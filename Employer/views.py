from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy

from django.views.generic.edit import FormView
from jalali_date import datetime2jalali, date2jalali
from .models import  Advertisement , Company , Manager
from .forms import NewAdvertisementForm , NewCompanyForm
# Create your views here.

def NewAd(request):
	form = NewAdvertisementForm(request.POST or None , user = request.user.email)
	if form.is_valid():
		form.save()
		return redirect("Home")
	context = {
	"form":form
	}
	return render(request , 'Employer/New_Ad.html' , context)




def NewCompany(request):
	if request.method == 'POST':
		form = NewCompanyForm(request.POST or None)
		if form.is_valid():
			company_name = form.cleaned_data.get('name')
			company_address = form.cleaned_data.get('address')
			company_underlie = form.cleaned_data.get('underlie')
			
			requested_manager = Manager.objects.get(email = request.user.username)

			Company.objects.create(name = company_name , address = company_address , underlie = company_underlie,manager = requested_manager  , valid = False)
			return redirect("Home")
	else:
		form = NewCompanyForm()
	context = {
	"form":form
	}
	return render(request , 'Employer/New_company.html' , context)