from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .views import *

from django.urls import reverse , resolve

from .forms import EmployeeRegister,LoginForm,RegisterForm
from Employee.models import EmployeeModel

# Create your tests here.

class TestViews(TestCase):
	employee_register_data = {
	'first_name':'test',
	'last_name':'test' ,
	'username':'test'  , 
	'password':'test'
	}

	login_data = {'username':'temporary' , 'password':'PaSs0wrd'}

	manager_register_data = {
	'name': 'test',
	'family': 'test',
	'email': 'test@test.com',
	'phone': 'test',
	'About': 'test',
	'password': 'test',
	're_password': 'test',
	}

	def setUp(self):
		User = get_user_model()
		User.objects.create_user('temporary','temporary@gmail.com' , 'PaSs0wrd')

	def test_employee_register(self):
		url = reverse('EmployeeRegister')
		response = self.client.post(url , data = self.employee_register_data)
		self.assertEquals(resolve(url).func.view_class , EmployeeRegisterView)
		self.assertEqual(response.status_code , 200)
		self.assertTrue(EmployeeRegister.is_valid)

	def test_login_for_all_users(self):
		url = reverse('Login')
		post_response = self.client.post(url , self.login_data)
		user = EmployeeRegister(data = self.employee_register_data)
		if user.is_valid():
			user.save()
		login_mimic_response = self.client.login(username='temporary', password='PaSs0wrd')
		extra_model = EmployeeModel.objects.create(employee = User.objects.get(username = 'temporary'))
		self.assertTrue(url)
		self.assertEqual(post_response.status_code , 302)
		self.assertTrue(login_mimic_response)
		self.assertTrue(user , user.is_valid)
		self.assertTrue(extra_model)
		self.assertEqual(resolve(url).func , LoginView)

	def test_manager_register(self):
		url = reverse('Register')
		response = self.client.post(url , self.manager_register_data)
		form = RegisterForm(response)
		extra_model = User.objects.create_user('manager')
		self.assertEqual(response.status_code , 200)
		self.assertTrue(form.is_valid)
		self.assertTrue(extra_model)