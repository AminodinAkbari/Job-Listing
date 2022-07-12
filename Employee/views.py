from django.contrib.auth import authenticate
from django.shortcuts import render , redirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import EditNameOrEmailForm, PersonalInfo_ResumeForm , ChangePassword_Employee
from Controllers.views import employee_owner_can_access
from Controllers.utils import Advertisement_time_left

from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView , ListView

from Employer.models import Manager , Applicant , Advertisement , Hire
from .models import EmployeeModel , Favorite
from django.contrib.auth.models import User

from django.contrib import messages
from django import forms

from Controllers.models import passGenerator
# Create your views here.

class UpdateResume(UpdateView):
	form_class = PersonalInfo_ResumeForm
	model = EmployeeModel
	template_name = 'Employee/CreateResume.html'

	def get_form_kwargs(self, *args, **kwargs):
		kwargs = super().get_form_kwargs(*args, **kwargs)
		kwargs['user'] = self.request.user
		return kwargs

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


class EditNameOrEmail_Employee(TemplateView):

	def get(self , request , *args , **kwargs):
		email_form = EditNameOrEmailForm(initial = {'first_name':request.user.first_name ,
		 'last_name':request.user.last_name , 'username':request.user.username} , user=request.user)
		pass_form = ChangePassword_Employee()
		context = {'form' : email_form , 'password_form':pass_form}
		return render(request , 'Employee/EditNameOrEmail-Employee.html' , context)

	def post(self, request, *args, **kwargs):
		current_user = User.objects.filter(id = request.user.id)
		if 'email-name' in request.POST:
			form = EditNameOrEmailForm(request.POST , user=request.user)
			password_form = ChangePassword_Employee()
			if form.is_valid():
				f_name = form.cleaned_data.get('first_name')
				l_name = form.cleaned_data.get('last_name')
				u_name = form.cleaned_data.get('username')
				current_user.update(first_name = f_name , last_name = l_name , username = u_name )
				messages.success(request , 'پروفایل شما بروزرسانی شد')
				return redirect(reverse('EditNameOrEmail-Employee' , kwargs={'pk' : request.user.id}))

		elif 'change-password' in request.POST:
			form = EditNameOrEmailForm(initial = {'first_name':request.user.first_name ,
			 'last_name':request.user.last_name , 'username':request.user.username})
			password_form = ChangePassword_Employee(request.POST , user=request)
			if password_form.is_valid():
				old = password_form.cleaned_data.get('old')
				new = password_form.cleaned_data.get('new')
				re_new = password_form.cleaned_data.get('re_new')
				user = User.objects.get(username = request.user.username)
				user.set_password(new)
				user.save()
				messages.success(request , 'رمز عبور شما به روز رسانی شد . لطفا دوباره وارد شوید')
				return redirect(reverse('Login'))
		return render(request , 'Employee/EditNameOrEmail-Employee.html' , {'form':form , 'password_form':password_form})

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
		context['time_left'] = Advertisement_time_left(obj.ad)
		return context

class EmployeeJobApply(ListView):
	model = Applicant
	template_name = 'Employee/employee-JobApply.html'
	def get_context_data(self):
		context = super().get_context_data()
		context ['title'] = 'رزومه های ارسالی'
		context['Applicants'] = Applicant.objects.filter(user = self.request.user)
		return context

class EmployeeJobMarked(ListView):
	model = Favorite
	paginate_by = 10
	template_name = 'Employee/employee-AdsMarked.html'
	def get_context_data(self):
		context = super().get_context_data()
		context ['title'] = 'رزومه های ارسالی'
		context['employee'] = get_object_or_404(EmployeeModel , employee = self.request.user)
		context['page_obj'] = Favorite.objects.filter(user = self.request.user)
		context['title'] = 'آگهی های نشان شده'
		return context

class HiresList(ListView):
	template_name = 'Employee/Hire-messages.html'
	def get_queryset(self):
		return Hire.objects.filter(user = self.request.user)
	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'پیشنهادهای همکاری'
		return context

@employee_owner_can_access
def AdUnsaved(request , pk , employee):
	try:
		ad = get_object_or_404(Favorite,user = request.user , ad_id = pk)
		ad.delete()
	except:
		return redirect('Home')
	return redirect(request.GET.get('next'))


def AdSaved(request , ad):
	if user_type is not None:
		return redirect('/')
	advertisement = get_object_or_404(Advertisement,id = ad)
	try:
		get_object_or_404(Favorite,user = request.user , ad = ad)
	except:
		Favorite.objects.create(user = request.user , ad = advertisement)
	return redirect(request.GET.get('next'))

def ApplicantView(request , ad):
	advertisement = get_object_or_404(Advertisement,id = ad)
	try:
		get_object_or_404(Applicant,user = request.user , ad = ad)
	except:
		Applicant.objects.create(user = request.user , ad = advertisement)
	return redirect('/')

def canceling_applicant(request , pk):
	try:
		target = get_object_or_404(Applicant,id = pk)
		if target.user == request.user:
			target.delete()
	except:
		return redirect('/')
	return redirect('/')
