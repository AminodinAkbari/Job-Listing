from django.shortcuts import render , redirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import PersonalInfo_ResumeForm
from Controllers.views import Who_is ,employee_owner_can_access

from django.views.generic.edit import FormView , UpdateView
from django.views.generic import DetailView

from Employer.models import Manager , Applicant , Advertisement
from .models import EmployeeModel , Favorite
from django.contrib.auth.models import User

from django.contrib import messages

# from django.utils import timezone
# now = timezone.now()
# Create your views here.

class UpdateResume(UpdateView):
	form_class = PersonalInfo_ResumeForm
	model = EmployeeModel
	template_name = 'Employee/CreateResume.html'

	def dispatch(self , request , *args , **kwargs):
		obj = self.get_object()
		is_a_manager = Manager.objects.filter(email = self.request.user.username).exists()
		if is_a_manager:
			return redirect('/Managers_Cant_Biuld_Resume')
		if obj.employee != self.request.user:
			return redirect('Home')
		return super(UpdateResume , self).dispatch(request , *args , **kwargs)

	def get_context_data(self , **kwargs):
		obj = self.get_object()
		context = super().get_context_data(**kwargs)
		context['user'] = obj
		context['title'] = 'رزومه ساز'
		return context

	def get_success_url(self):
		obj = self.get_object()
		messages.success(self.request , 'تغییرات با موفقیت ذخیره شد')
		return reverse_lazy('UpdateResume' , kwargs = {'pk':obj.id})

import datetime
today = datetime.datetime.now().date()
class ApplicantDetail(DetailView):
	model = Applicant
	template_name = 'Employee/Applicant-detail.html'

	def dispatch(self ,request , *args, **kwargs):
		obj = self.get_object()
		if obj.user.username != request.user.username:
			return redirect('/')
		return super(ApplicantDetail , self).dispatch(request , *args , **kwargs)

	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['employee'] = EmployeeModel.objects.filter(employee = self.request.user).first()
		obj = self.get_object()
		# context['time_left'] = obj.ad.expired_in.day-now.day
		return context

@Who_is
def ApplicantView(request , ad , user_type):
	if user_type is not None:
		return redirect('/')
	advertisement = Advertisement.objects.get(id = ad)
	try:
		Applicant.objects.get(user = request.user , ad = ad)
	except:
		Applicant.objects.create(user = request.user , ad = advertisement)
	return redirect('/')

@Who_is
def canceling_applicant(request , pk , user_type):
	if user_type is None:
		try:
			target = Applicant.objects.get(id = pk)
			if target.user == request.user:
				target.delete()
		except:
			return redirect('/')
	return redirect('/')


@Who_is
def FavoriteView(request , ad , user_type):
	if user_type is not None:
		return redirect('/')
	advertisement = Advertisement.objects.get(id = ad)
	try:
		Favorite.objects.get(user = request.user , ad = ad)
	except:
		Favorite.objects.create(user = request.user , ad = advertisement)
	return redirect('/')

@employee_owner_can_access
def EmployeeJobApply(request , pk , employee):
	context = {}
	applicants = Applicant.objects.filter(user = request.user)
	context['employee'] = employee
	context['Applicants'] = applicants
	context['title'] = 'رزومه های ارسالی'
	return render(request , 'Employee/employee-JobApply.html' , context)

@employee_owner_can_access
def AdSaved(request , pk ,employee):
	context = {}
	ads = Favorite.objects.filter(user = request.user)
	context['employee'] = employee
	context['Ads'] = ads
	return render(request , 'Employee/employee-AdsMarked.html' , context)

def AdUnsaved(request , pk):
	ad = Favorite.objects.get(user = request.user , ad_id = pk)
	ad.delete()
	return redirect(reverse('AdsSaved' , kwargs = {'pk':request.user.id}))
