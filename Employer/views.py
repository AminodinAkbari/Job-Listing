from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .forms import EditManagerInfoForm,UpdatePasswordManagersForm

from django.contrib import messages

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from jalali_date import datetime2jalali, date2jalali
from .models import  Advertisement , Company , Manager

from Controllers.models import passGenerator


from .forms import (
NewAdvertisementForm,
NewCompanyForm,
EditAdInfoForm,
EditCompanyForm,
)

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

        context['object'] =  manager
        context['companies'] = company
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

def UpdatePasswordManager(request):
    update_password_form = UpdatePasswordManagersForm()
    if request.method == "POST":
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
    context = {
    'UpdatePassword':update_password_form,
    'suggest_password':passGenerator(10)
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
            messages.success(request , 'شرکت شما با موفقیت ثبت شد. مدیر وب سایت حال باید وب سایت صحت وجود این شرکت را بررسی نماید' , extra_tags = 'NewCompanyCreated')
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