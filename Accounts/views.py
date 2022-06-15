from django.shortcuts import render , redirect
from django.views.generic.edit import FormView , UpdateView
from django.contrib import messages

from django.urls import reverse,reverse_lazy
from .forms import RegisterForm , LoginForm , EmployeeRegister
from django.contrib.auth import authenticate, login,logout

from Controllers.models import passGenerator
from django.contrib.auth.models import User
from Employer.models import Manager
from Employee.models import EmployeeModel
# Create your views here.

class RegisterView(FormView):
	template_name = 'Accounts/register.html'
	model = Manager
	form_class = RegisterForm

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('Home')
		return super(RegisterView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.method == "POST":
			context['form'] = RegisterForm(self.request.POST ,self.request.FILES)
		else:
			context['form'] = RegisterForm()
		return context

	def get_success_url(self):
		form = RegisterForm(self.request.POST,self.request.FILES)
		form.save()

		name = self.request.POST['name']
		family = self.request.POST['family']
		email = self.request.POST['email']
		password = self.request.POST['password']

		creating_user = User.objects.create(username = email , email = email , first_name = name , last_name = family)
		creating_user.set_password(password)
		creating_user.save()

		user = authenticate(self.request ,username = email , password = password)

		if user is not None:
			login(self.request , user)
			return reverse('Home')

		return reverse('Register')

def LoginView(request):
	if request.user.is_authenticated:
		return redirect('Home')
	login_form = LoginForm(request.POST or None)
	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		user = authenticate(request ,username = username , password = password)
		if user is not None:

			login(request , user)
			try:
				return redirect(request.GET.get('next'))
			except:
				return redirect('/')
		else:
			try:
				user_exist = User.objects.get(username = username)
				login_form.add_error('password','رمز عبور اشتباه است')
			except:
				login_form.add_error('username','کاربری با این ایمیل یافت نشد')
	context = {
	'login_form':login_form
	}
	return render(request , 'Accounts/login.html' , context)

def LogoutView(request):
	logout(request)
	return redirect('/')


class EmployeeRegisterView(FormView):
	form_class = EmployeeRegister
	model = User
	template_name = 'Employee/employee-register.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('Home')
		return super(EmployeeRegisterView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user=form.save()
		user.set_password(self.request.POST['password'])
		form.save()
		EmployeeModel.objects.create(employee = user)
		return super(EmployeeRegisterView, self).form_valid(form)

	def get_success_url(self):
		username = self.request.POST['username']
		password = self.request.POST['password']
		user = authenticate(self.request , username = username , password = password)

		if user:
			login(self.request , user)
		return reverse_lazy('Home')
