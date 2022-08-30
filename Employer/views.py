from django.shortcuts import render,redirect , get_object_or_404
import django
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import EditManagerInfoForm,UpdatePasswordManagersForm,EditEmailEmployer,NewHireForm

from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView , CreateView , FormView
from django.views.generic.base import View , TemplateView

from .models import  Advertisement , Company , Manager , Applicant , Hire , AdminMessage
from Employee.models import EmployeeModel

from Controllers.models import passGenerator , states_iran


from .forms import (
NewAdvertisementForm,
NewCompanyForm,
EditAdInfoForm,
EditCompanyForm,
)

from django.utils import timezone
now = timezone.now()

class ManagerPanel(DetailView):
    model = Manager
    template_name = "employer-dashboard/ManagerPanel.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.email != self.request.user.username:
            return redirect('/')
        return super(ManagerPanel, self).dispatch(request, *args, **kwargs)

    def get_context_data(self,*args , **kwargs):
        context = super().get_context_data(**kwargs)
        manager = Manager.objects.filter(email = self.request.user.username).first()
        company = Company.objects.filter(manager = manager.id)
        c_valids = company.filter(valid=True)
        c_invalids = len(company) - len(c_valids)
        applicants = Applicant.objects.filter(ad__company__manager__email = self.request.user.username)
        
        employees = EmployeeModel.objects.all()
        messages = AdminMessage.objects.filter(enable = True).order_by('created_at')
        new_messages = AdminMessage.objects.filter(enable = True , new=True)
        
        if company:
            ads= Advertisement.objects.none()
            for i in company:
                ads = ads|i.company.all()
            context['ads'] = ads.order_by('id')

        context['states_iran'] = states_iran
        context['object'] =  manager
        context['companies'] = company
        context['valid_companies'] = c_valids
        context['invalid_companies'] = c_invalids
        context['apps'] = applicants
        context['messages'] = messages
        context['new_messages'] = new_messages
        context['title'] = 'پنل مدیریت'
        context['now'] = now
        return context

class MessageDetail(DetailView):
    model = AdminMessage
    template_name = 'Employer/MessageDetail.html'

    def dispatch(self , *args , **kwargs):
        obj=self.get_object()
        if obj.new == True:
            obj.new = False
            obj.save()
        return super().dispatch(*args , **kwargs)

class ADApplicants(DetailView):
    model = Applicant
    template_name = 'Employer/ADApplicants.html'

    def get_context_data(self , *args , **kwargs):
        context_list = super().get_context_data(*args , **kwargs)
        ads = get_object_or_404(Advertisement , id = self.kwargs['pk'])
        context_list['ads'] = ads
        return context_list

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

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['title'] = 'آگهی جدید'
        c = Company.objects.filter(manager__email = self.request.user.username , valid=True)
        context['companies'] = c
        return context

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

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['title'] = f'ثبت شرکت جدید'
        return context


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
            if applicant.seen_at is None:
                applicant.seen_at = django.utils.timezone.now()
            applicant.save()
    if request.method == 'POST' and 'accepted' in request.POST or 'rejected' in request.POST:
        if 'accepted' in request.POST:
            applicant.status = 'accepted'

        elif 'rejected' in request.POST:
            applicant.status = 'rejected'

        applicant.determine_at = django.utils.timezone.now()
        applicant.save()
        return redirect('/')
        
    context = {
    'object' : employee ,
    'manager':manager,
    'title':'جزئیات رزومه ارسالی'
    }
    
    if employee.skills:
        context['employee_skills'] = employee.skills.split('/')

    return render(request , 'Employer/EmployeeDetermine.html' , context)


class NewHire(CreateView):
    form_class = NewHireForm
    model = Hire
    template_name = 'Employer/NewHire.html'

    def get_context_data(self , *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['item'] = get_object_or_404(EmployeeModel,id = self.kwargs['employee_id'])
        return context

    def form_valid(self , form):
        employee = get_object_or_404(EmployeeModel,id = self.kwargs['employee_id'])
        check_already_hire = Hire.objects.filter(user = employee.employee , ad = form.instance.ad).exists()
        check_already_is_applicant = Applicant.objects.filter(user_id = employee.employee.id , ad = form.instance.ad).exists()
        if check_already_hire:
            messages.success(self.request , 'شما قبلا برای این کارجو درخواست فرستاده اید')
            return redirect('/')
        elif check_already_is_applicant :
            messages.success(self.request , 'کارجو در حال حاضر برای این آگهی درخواست فرستاده است . لطفا پنل مدیریت خود را چک کنید')
            return redirect('/')
        else:
            form.instance.user = employee.employee
            return super(NewHire , self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request , 'پیام شما به کارجو ارسال شد . وضعیت درخواست را میتوانید در پنل خود مشاهده کنید')
        return reverse_lazy('Home')
