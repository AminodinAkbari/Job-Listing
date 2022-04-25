from django.shortcuts import render , redirect
from django.views.generic.edit import FormView
from Employer.models import Manager
from django.urls import reverse
from .forms import RegisterForm , LoginForm
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.models import User
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
		context['form'] = RegisterForm(self.request.POST ,self.request.FILES)
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
