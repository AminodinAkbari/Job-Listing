from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import EditManagerInfoForm,UpdatePasswordManagersForm,EditEmailEmployer

from django.contrib import messages

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import  Advertisement , Company , Manager , Applicant
from Employee.models import EmployeeModel

from Controllers.models import passGenerator
from Controllers.views import Who_is


from .forms import (
NewAdvertisementForm,
NewCompanyForm,
EditAdInfoForm,
EditCompanyForm,
)

from django.utils import timezone
now = timezone.now()
# Create your views here.

class ManagerPanel(DetailView):
    model = Manager
    template_name = "Employer/ManagerPanel.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.email != self.request.user.username:
            return redirect('/')
        return super(ManagerPanel, self).dispatch(request, *args, **kwargs)

    def get_context_data(self,*args , **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            manager = Manager.objects.get(email = self.request.user.username)
            company = Company.objects.filter(manager = manager.id)
        except:
            manager = None

        applicants = Applicant.objects.filter(ad__company__manager__email = self.request.user.username)

        context['object'] =  manager
        context['companies'] = company
        context['applicants'] = applicants
        context['title'] = 'پنل مدیریت'
        return context

class EditMangerInfo(UpdateView):
    form_class = EditManagerInfoForm
    model = Manager
    template_name = 'Employer/EditManagersInfo.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.email != self.request.user.username:
            return redirect('/')
        return super(EditMangerInfo, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request , 'تغییرات ذخیره شد')
        current_manager = Manager.objects.get(email = self.request.user.username)
        return reverse_lazy('ManagerPanel', kwargs={'pk': current_manager.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'تغییر اطلاعات (کارفرما)'
        context['user'] = Manager.objects.get(email = self.request.user.username)
        return context

class EditAdView(UpdateView):
    form_class = EditAdInfoForm
    model = Advertisement
    template_name = 'Employer/EditAdInfo.html'

    def dispatch(self, request, *args, **kwargs):
        Ad = self.get_object()
        if Ad.company.manager != Manager.objects.get(email = self.request.user.username):
            return redirect('Home')
        return super(EditAdView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request , 'تغییرات ذخیره شد')
        current_manager = Manager.objects.get(email = self.request.user.username)
        return reverse_lazy('ManagerPanel', kwargs={'pk': current_manager.id})

@Who_is
def UpdatePasswordManager(request , user_type):
    if user_type is None:
        return redirect('Home')
    update_password_form = UpdatePasswordManagersForm()
    edit_email_form = EditEmailEmployer(initial = {'email' : request.user.username})
    if request.method == "POST" and 'update-pass' in request.POST:
        update_password_form = UpdatePasswordManagersForm(request.POST)
        if update_password_form.is_valid():
            old_password = update_password_form.cleaned_data.get('old_password')
            new_password = update_password_form.cleaned_data.get('new_password')
            re_new_password = update_password_form.cleaned_data.get('re_new_password')

            user_exist = User.objects.get(username = request.user.email)
            if user_exist:
                user = authenticate(request ,username = request.user.username , password = old_password)
                if user is not None:
                    if old_password == new_password:
                        update_password_form.add_error('old_password' ,'رمز عبور جدید باید با رمز عبور حال حاضر تفاوت داشته باشد')
                    else:
                        user_exist.set_password(new_password)
                        user_exist.save()
                        messages.success(request , 'رمز عبور شما با موفقیت تغییر کرد')
                        return redirect('/login')
                else:
                    update_password_form.add_error('old_password' , 'رمز عبور حال حاضر شما اشتباه است !')
    if request.method == "POST" and 'update-email' in request.POST:
        edit_email_form = EditEmailEmployer(request.POST)
        if edit_email_form.is_valid():
            email = edit_email_form.cleaned_data.get('email')
            try:
                manager_user = User.objects.get(id = request.user.id)
                manager_model = user_type
                if manager_user and manager_model:
                    manager_user.username = email
                    manager_model.email = email
                    manager_user.save()
                    manager_model.save()
                    messages.success(request , 'پروفایل شما آپدیت شد')
            except:
                messages.error(request , 'ایمیل معتبر نیست یا قبلا در سایت ثبت شده است')
        else:
            messages.error(request , 'ایمیل معتبر نیست یا قبلا در سایت ثبت شده است')


    context = {
    'UpdatePassword':update_password_form,
    'UpdateEmail':edit_email_form,
    'suggest_password':passGenerator(10),
    'title':'تنظیمات حساب کاربری',
    }

    return render(request , 'Employer/UpdateManagersPassword.html' , context)


def NewAd(request):
    form = NewAdvertisementForm(request.POST or None , user = request.user.email)
    if form.is_valid():
        form.save()
        messages.success(request , 'آگهی شما با موفقیت ایجاد شد' , extra_tags = 'NewAdCreated')
        return redirect("Home")
    context = {
    "form":form
    }
    return render(request , 'Employer/New_Ad.html' , context)


def NewCompany(request):
    if request.method == 'POST':
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data.get('name')
            company_address = form.cleaned_data.get('address')
            company_underlie = form.cleaned_data.get('underlie')

            requested_manager = Manager.objects.get(email = request.user.username)

            Company.objects.create(name = company_name , address = company_address , underlie = company_underlie,manager = requested_manager  , valid = False)
            messages.success(request , 'شرکت شما با موفقیت ثبت شد . حال باید مدیر وب سایت وجود خارجی این شرکت را تایید کند' , extra_tags = 'NewCompanyCreated')
            return redirect("Home")
    else:
        form = NewCompanyForm()
    context = {
    "form":form
    }
    return render(request , 'Employer/New_company.html' , context)

def DeleteAd(request , pk ,**kwargs):
    manager = Manager.objects.filter(email = request.user.username).first()
    ad = Advertisement.objects.get(company__manager = manager.id , id=pk)
    print(manager)
    if manager is not None and ad is not None:
        try:
            print(ad)
            ad.delete()
        except:
            messages.error(request , 'آگهی در پایگاه داده پیدا نشد')
    return HttpResponseRedirect(reverse_lazy('ManagerPanel' , kwargs={'pk': manager.id}))

class EditCompanyView(UpdateView):
    form_class = EditCompanyForm
    model = Company
    template_name = 'Employer/EditCompanyInfo.html'

    def dispatch(self , request , *args):
        obj = self.object
        if obj.manager.email != request.user.username:
            return redirect('Home')
        return super(EditCompanyView , self).dispatch(request , *args)

    def get_success_url(self):
        current_manager = Manager.objects.get(email = self.request.user.username)
        messages.success(self.request , 'تغییرات ذخیره شد')
        current_manager = Manager.objects.get(email = self.request.user.username)
        return reverse_lazy('ManagerPanel', kwargs={'pk': current_manager.id})

def DeleteCompany(request , pk):
    manager = Manager.objects.filter(email = request.user.username).first()
    company= Company.objects.get(manager = manager.id , id=pk)
    if manager is not None and company is not None:
        try:
            company.delete()
        except:
            messages.error(request , 'خطایی رخ داد')
    return HttpResponseRedirect(reverse_lazy('ManagerPanel' , kwargs={'pk': manager.id}))

def determine_the_status(request , pk,adver_id):
    employee = EmployeeModel.objects.filter(id = pk).first()
    manager = Manager.objects.get(email = request.user.username)
    if employee is not None:
        applicant = Applicant.objects.filter(ad__id = adver_id , user = employee.employee).first()
        if applicant is not None:
            applicant.status = "seen"
            applicant.created_at = now
            applicant.save()
    if request.method == 'POST' and applicant is not None:
        if request.method == 'POST':
            if request.POST['determine'] == 'accept':
                applicant.status = 'accepted'
                applicant.save()
                return redirect('/')
            else:
                applicant.status = 'rejected'
                applicant.save()
                return redirect('/')
    context = {
    'object' : employee ,
    'employee_skills' : employee.skills.split('/'),
    'manager':manager,
    'title':'جزئیات رزومه ارسالی'
    }
    return render(request , 'Employer/EmployeeDetermine.html' , context)
