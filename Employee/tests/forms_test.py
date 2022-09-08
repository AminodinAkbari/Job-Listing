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
		self.user = User.objects.create_user('test@gmail.com' ,'amin@gmail.com' ,'aminamin')
		user = User.objects.create_user('amin@gmail.com' ,'amin@gmail.com' ,'aminamin')
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
		print(self.user.id)
		form = PersonalInfo_ResumeForm(data = self.unvalid_user , user = self.user)
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['phone'] , ['این شماره تلفن قبلا در سایت ثبت نام شده !'])

	def test_save_and_valid_resume_update(self):
		form = PersonalInfo_ResumeForm(data = self.valid_user)
		form.is_valid()
		user = form.save()
		self.assertTrue(form.is_valid())
		self.assertIsInstance(user , EmployeeModel)

#----------------Change Email Employee Tests --------------------
	def test_email_form_requireds(self):
		change_email_form_EMPTY = EditNameOrEmailForm(data = {})
		self.assertEqual(change_email_form_EMPTY.errors['first_name'] , ['نمیتواند خالی باشد'])
		self.assertEqual(change_email_form_EMPTY.errors['last_name'] , ['نمیتواند خالی باشد'])
		self.assertEqual(change_email_form_EMPTY.errors['username'] , ['نمیتواند خالی باشد'])

	def test_duplicate_change_email(self):
		duplicate_email_form = EditNameOrEmailForm(data = {'first_name':'test' , 'last_name' : 'test' ,
		 'username':'amin@gmail.com'} , user = self.user)
		self.assertEqual(duplicate_email_form.errors['username'] , ['این ایمیل قبلا در سایت ثبت نام شده است'])

	def test_invalid_change_email(self):
		invalid_change_email_form = EditNameOrEmailForm(data = {'first_name':'test' , 'last_name' : 'test' ,
		 'username':'amin@gmail.wrong'} , user = self.user)
		self.assertEqual(invalid_change_email_form.errors['username'] , ['ایمیل معتبر نیست لطفا از درست وارد کردن ایمیل مطمئن شوید'])

	def test_valid_change_email_form(self):
		change_email_form_FULL = EditNameOrEmailForm(data = {'first_name':'test' , 'last_name' : 'test' , 'username':'test@gmail.com'})
		print(change_email_form_FULL.errors)
		self.assertTrue(change_email_form_FULL.is_valid())

#-----------------------Change Password Form Test ---------------------------
	def test_passwords_form_errors(self):
		change_password_form_EMPTY = ChangePassword_Employee(data = {})
		self.assertEqual(change_password_form_EMPTY.errors['old'] , ['نمی تواند خالی باشد'])
		self.assertEqual(change_password_form_EMPTY.errors['new'] , ['نمی تواند خالی باشد'])
		self.assertEqual(change_password_form_EMPTY.errors['re_new'] , ['نمی تواند خالی باشد'])

	def change_password_clean_methods(self):
		form1 = ChangePassword_Employee(data = {'old' : '1234' , 'new':'123' , 're_new' : '123'})
		form2 = ChangePassword_Employee(data = {'new':'1234567890' , 're_new':'1234567890' , 'old':'1234567890'})
		self.assertEqual(form1.errors['new'] , ['کلمه عبور باید حداقل 8 کاراکتر باشد'])
		self.assertEqual(form2.errors['new'] , ['رمز عبور جدید باید متفاوت با رمز عبور قبلی باشد'])

	def test_valid_pass_form(self):
		healthy_change_password_form = ChangePassword_Employee(data = {'new':'1234567890' , 're_new':'1234567890' , 'old':'123456789'})
		self.assertTrue(healthy_change_password_form.is_valid())
