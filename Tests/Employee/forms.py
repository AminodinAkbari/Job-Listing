from django.test import TestCase
from Employee.models import EmployeeModel
from Employee.views import UpdateResume
from Employee.forms import EditNameOrEmailForm , PersonalInfo_ResumeForm , ChangePassword_Employee
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class TestForms(TestCase):

	def setUp(self):
		user = User.objects.create_user('amin','amin@gmail.com' , 'PaSs0w0rd')
		EmployeeModel.objects.create(employee = user , phone = self.unvalid_user['phone'],
		sex = self.unvalid_user['sex'] , marital_status = self.unvalid_user['marital_status'] ,
		employee_soldier_ship = self.unvalid_user['employee_soldier_ship'] , birth = self.unvalid_user['birth']
		)


	valid_user = {
	'employee' : User.objects.all().first(),
	'phone' : '09182064916',
	'sex' : 'Male',
	'marital_status':'Married',
	'employee_soldier_ship' : 'D',
	'birth' : '2022-2-3'
	}

	unvalid_user = {
	'employee' : User.objects.all().first(),
	'phone' : '12345678901',
	'sex' : 'Male',
	'marital_status':'Married',
	'employee_soldier_ship' : 'D',
	'birth' : '2022-2-3'
	}

	def test_empty_resume_fields(self):
		user = User.objects.all().first()
		form = PersonalInfo_ResumeForm(data = {})
		self.assertEqual(form.errors["phone"], ["شماره تلفن ضروری است"])
		self.assertEqual(form.errors["sex"], ["لطفا جنسیت خود را مشخص کنید"])
		self.assertEqual(form.errors["marital_status"], ["لطفا وضعیت تأهل خود را مشخص کنید"])
		self.assertEqual(form.errors["employee_soldier_ship"], ["وضعیت خدمت شما نمیتواند خالی باشد"])
		self.assertEqual(form.errors["birth"], ["تاریخ تولد الزامی است"])

	def test_resume_clean_phone(self):
		form = PersonalInfo_ResumeForm(data = self.unvalid_user)
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['phone'] , ['این شماره تلفن قبلا در سایت ثبت نام شده !'])

	def test_save_and_valid_resume_update(self):
		form = PersonalInfo_ResumeForm(data = self.valid_user)
		form.is_valid()
		user = form.save()
		self.assertTrue(form.is_valid())
		self.assertIsInstance(user , EmployeeModel)

class TestChangeEmailAndPass_Employee(TestCase):

	def test_email_form_errors(self):
		change_email_form_EMPTY = EditNameOrEmailForm(data = {})
		self.assertEqual(change_email_form_EMPTY.errors['first_name'] , ['نمیتواند خالی باشد'])
		self.assertEqual(change_email_form_EMPTY.errors['last_name'] , ['نمیتواند خالی باشد'])
		self.assertEqual(change_email_form_EMPTY.errors['username'] , ['نمیتواند خالی باشد'])

	def test_valid_email_form(self):
		change_email_form_FULL = EditNameOrEmailForm(data = {'first_name':'test' , 'last_name' : 'test' , 'username':'test'})
		self.assertTrue(change_email_form_FULL.is_valid())

	def test_passwords_form_errors(self):
		change_password_form_EMPTY = ChangePassword_Employee(data = {})
		clean_methodes_change_password_form = ChangePassword_Employee(data = {'new' : '123' , 'old':'123' , 're_new' : '123'})
		self.assertEqual(change_password_form_EMPTY.errors['old'] , ['نمی تواند خالی باشد'])
		self.assertEqual(change_password_form_EMPTY.errors['new'] , ['نمی تواند خالی باشد'])
		self.assertEqual(change_password_form_EMPTY.errors['re_new'] , ['نمی تواند خالی باشد'])
		self.assertTrue(clean_methodes_change_password_form.errors)

	def test_same_new_password_and_old_password(self):
		form = ChangePassword_Employee(data = {'new':'1234567890' , 're_new':'1234567890' , 'old':'1234567890'})
		self.assertEqual(form.errors['new'] , ['رمز عبور جدید باید متفاوت با رمز عبور قبلی باشد'])

	def test_valid_pass_form(self):
		healthy_change_password_form = ChangePassword_Employee(data = {'new':'1234567890' , 're_new':'1234567890' , 'old':'123456789'})
		self.assertTrue(healthy_change_password_form.is_valid())
