from django.shortcuts import render,redirect , get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import EditManagerInfoForm,UpdatePasswordManagersForm,EditEmailEmployer,NewHireForm

from django.contrib import messages

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView , CreateView , FormView
from django.views.generic.base import View , TemplateView

from .models import  Advertisement , Company , Manager , Applicant , Hire
from Employee.models import EmployeeModel

from Controllers.models import passGenerator


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
            company = None

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

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(EditMangerInfo, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

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
        context['user'] = get_object_or_404(Manager,email = self.request.user.username)
        return context

class EditAdView(UpdateView):
    form_class = EditAdInfoForm
    model = Advertisement
    template_name = 'Employer/EditAdInfo.html'

    def dispatch(self, request, *args, **kwargs):
        Ad = self.get_object()
        if Ad.company.manager.email != self.request.user.username:
            return redirect('Home')
        return super(EditAdView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ویرایش اطلاعات آگهی'
        return context

    def get_success_url(self):
        messages.success(self.request , 'تغییرات ذخیره شد')
        current_manager = Manager.objects.get(email = self.request.user.username)
        return reverse_lazy('ManagerPanel', kwargs={'pk': current_manager.id})

class UpdatePasswordManager(TemplateView):
    template_name = 'Employer/UpdateManagersPassword.html'

    def get(self , request , *args , **kwargs):
        password_form = UpdatePasswordManagersForm(user = request.user)
        email_form = EditEmailEmployer(initial = {'email':request.user.username})
        context = {'UpdatePassword':password_form , 'UpdateEmail' : email_form}
        return render(request , 'Employer/UpdateManagersPassword.html' , context)

    def post(self, request, *args, **kwargs):
        current_user = get_object_or_404(User,id = request.user.id)
        if 'update-email' in request.POST:
            password_form = UpdatePasswordManagersForm()
            email_form = EditEmailEmployer(request.POST , user=request.user)
            if email_form.is_valid():
                email = email_form.cleaned_data.get('email')
                user = User.objects.get(username = request.user.username)
                manager = Manager.objects.get(email = user.username)
                user.username = email
                manager.email = email
                user.save()
                manager.save()
                messages.success(request , 'پروفایل شما آپدیت شد')
                return redirect(reverse('ManagerPanel' , kwargs={'pk':manager.id}))

        elif 'update-pass' in request.POST:
            password_form = UpdatePasswordManagersForm(request.POST , user = request.user)
            email_form = EditEmailEmployer(initial = {'email':request.user.username})
            if password_form.is_valid():
                old_password = password_form.cleaned_data.get('old_password')
                new_password = password_form.cleaned_data.get('new_password')
                user_exist = User.objects.get(username = request.user.username)
                current_user.set_password(new_password)
                current_user.save()
                messages.success(request , 'رمز عبور شما با موفقیت تغییر کرد')
                return redirect(reverse('Login'))

        return render(request , 'Employer/UpdateManagersPassword.html' , {'UpdatePassword':password_form , 'UpdateEmail' : email_form})

class NewAd(FormView):
    form_class = NewAdvertisementForm
    model = Advertisement
    template_name = 'Employer/New_Ad.html'
    success_url = '/'

    def get_form_kwargs(self):
        initial = super().get_form_kwargs()
        initial['user'] = self.request.user.username
        return initial

    def form_valid(self , form):
        form.save()
        messages.success(self.request , 'آگهی شما با موفقیت ایجاد شد' , extra_tags = 'NewAdCreated')
        form = super().form_valid(form)
        return form

class NewCompany(FormView):
    form_class = NewCompanyForm
    template_name = 'Employer/New_company.html'
    success_url   = '/'

    def form_valid(self , form):
        requested_manager = Manager.objects.get(email = self.request.user.username)
        print(requested_manager.email)
        form.instance.manager = requested_manager
        form.save()
        print(form.instance.manager)
        messages.success(self.request , 'شرکت شما با موفقیت ثبت شد . حال باید مدیر وب سایت وجود خارجی این شرکت را تایید کند' , extra_tags = 'NewCompanyCreated')
        return super().form_valid(form)


def DeleteAd(request , pk ,**kwargs):
    manager = Manager.objects.filter(email = request.user.username).first()
    ad = get_object_or_404(Advertisement,company__manager = manager.id , id=pk)
    if manager is not None and ad:
        ad.delete()
    return HttpResponseRedirect(reverse_lazy('ManagerPanel' , kwargs={'pk': manager.id}))

class EditCompanyView(UpdateView):
    form_class = EditCompanyForm
    model = Company
    template_name = 'Employer/EditCompanyInfo.html'

    def dispatch(self , request , *args, **kwargs):
        obj = self.get_object()
        if obj.manager.email != request.user.username:
            return redirect('Home')
        return super(EditCompanyView , self).dispatch(request , *args , **kwargs)

    def get_success_url(self):
        current_manager = Manager.objects.get(email = self.request.user.username)
        messages.success(self.request , 'تغییرات ذخیره شد')
        current_manager = Manager.objects.get(email = self.request.user.username)
        return reverse_lazy('ManagerPanel', kwargs={'pk': current_manager.id})

    def get_context_data(self , **kwargs):
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(id = obj.id)
        context['title'] = 'ویرایش اطلاعات شرکت'
        return context


def DeleteCompany(request , pk):
    manager = Manager.objects.filter(email = request.user.username).first()
    company= get_object_or_404(Company,manager = manager.id , id=pk)
    if manager is not None and company is not None:
        company.delete()
    return HttpResponseRedirect(reverse_lazy('ManagerPanel' , kwargs={'pk': manager.id}))

def determine_the_status(request , pk,adver_id):
    employee = get_object_or_404(EmployeeModel,id = pk)
    manager = get_object_or_404(Manager,email = request.user.username)
    if employee and manager:
        applicant = Applicant.objects.filter(ad__id = adver_id , user = employee.employee).first()
        if applicant:
            applicant.status = "seen"
            # The Date is Change But This Is'nt Correct Way
            # Later Should Fix This
            applicant.created_at = now
            #-------------------------
            applicant.save()
    if request.method == 'POST' and applicant:
        if 'accepted' in request.POST:
            applicant.status = 'accepted'
            applicant.save()
            return redirect('/')
        elif 'rejected' in request.POST:
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


class NewHire(CreateView):
    form_class = NewHireForm
    model = Hire
    template_name = 'Employer/NewHire.html'

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['item'] = get_object_or_404(EmployeeModel,id = self.kwargs['employee_id']).first()
        return context

    def form_valid(self , form):
        employee = EmployeeModel.objects.get(id = self.kwargs['employee_id'])
        check = Hire.objects.filter(user = employee.employee , ad = form.instance.ad).exists()
        if check:
            messages.success(self.request , 'شما قبلا برای این کارجو درخواست فرستاده اید')
            return redirect('/')
        else:
            form.instance.user = employee.employee
            return super(NewHire , self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request , 'پیام شما به کارجو ارسال شد . وضعیت درخواست را میتوانید در پنل خود مشاهده کنید')
        return reverse_lazy('Home')
