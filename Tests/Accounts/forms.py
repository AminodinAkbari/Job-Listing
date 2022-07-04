from django.test import TestCase
from Accounts.forms import RegisterForm , LoginForm , EmployeeRegister
from Employer.models import Manager
from Employee.models import EmployeeModel
from django.contrib.auth.models import User
from Tests.Employer.forms import TestEmployerForms
class TestAccountForms(TestCase):
    valid_register = {
    'username' : 'AminEmail@gmail.com',
    'first_name' : 'Amin',
    'last_name' : 'Akbari',
    'password' : '123456789',
    're_password' : '123456789',
    }
    unvalid_register = {
    'name':'amin',
    'family':'akbari',
    'phone' : '123',
    'About' : 'test',
    'email' : 'temp@gmail.ooo',
    }

    unvalid_register_employee_invalid_email = {
    'username' : 'test',
    'password' : '2012',
    're_password' : '123',
    'first_name' : 'amin' ,
    'last_name' : 'akbari'
    }

    unvalid_register_employee_duplicate_email = {
    'username' : 'amin@gmail.com',
    'password' : '2012',
    're_password' : '123',
    'first_name' : 'amin' ,
    'last_name' : 'akbari'
    }

    unvalid_user = {
    'employee' : User.objects.all().first(),
    'phone' : '12345678901',
    'sex' : 'Male',
    'marital_status':'Married',
    'employee_soldier_ship' : 'D',
    'birth' : '2022-2-3'
    }

    def setUp(self):
        self.user = User.objects.create_user('amin@gmail.com' ,'amin@gmail.com' ,'aminamin')
        Manager.objects.create(name = TestEmployerForms.valid_manager['name'] , family = TestEmployerForms.valid_manager['family'],
        email = TestEmployerForms.unvalid_manager['email'] , phone = '09182061234'
        )
        EmployeeModel.objects.create(employee = self.user , phone = self.unvalid_user['phone'],
        sex = self.unvalid_user['sex'] , marital_status = self.unvalid_user['marital_status'] ,
        employee_soldier_ship = self.unvalid_user['employee_soldier_ship'] , birth = self.unvalid_user['birth']
        )
#-----------Register Form-----------------------
    def test_empty_register_form(self):
        form = RegisterForm(data = {})
        self.assertEqual(form.errors['name'] , ['نمیتواند خالی باشد'])

    def test_clean_methods(self):
        unvalidform = RegisterForm(data = self.unvalid_register)
        dupolicateform = RegisterForm(data = TestEmployerForms.unvalid_manager)
        self.assertEqual(dupolicateform.errors['phone'] , ['این شماره قبلا در سایت ثبت شده است !'])
        self.assertEqual(dupolicateform.errors['email'] , ['این ایمیل قبلا در سایت ثبت شده است !'])
        self.assertEqual(unvalidform.errors['phone'] , ['شماره وارد شده صحیح نیست'])
        self.assertEqual(unvalidform.errors['email'] , ['ایمیل معتبر نیست لطفا از درست وارد کردن ایمیل مطمئن شوید'])

    def test_valid_and_save(self):
        form = RegisterForm(data = TestEmployerForms.valid_manager)
        print(form.errors)
        form.is_valid()
        user = form.save()
        self.assertIsInstance(user, Manager)
        self.assertTrue(form.is_valid())
#----------- Login Form ----------------
    def test_valid_login_form(self):
        form = LoginForm(data = {'username':'username' , 'password':'password'})
        self.assertTrue(form.is_valid())

# ---------- EmployeeRegister Form -------
    def test_unvalid_employee_register_form(self):
        invalid_email_form = EmployeeRegister(data = self.unvalid_register_employee_invalid_email)
        duplicate_email_form = EmployeeRegister(data = self.unvalid_register_employee_duplicate_email)
        bad_password_form = EmployeeRegister(data = self.unvalid_register_employee_invalid_email)
        self.assertEqual(invalid_email_form.errors['username'] , ['ایمیل معتبر نیست لطفا از درست وارد کردن ایمیل مطمئن شوید'])
        self.assertEqual(duplicate_email_form.errors['username'] , ['این ایمیل قبل در سایت ثبت نام شده است'])
        self.assertEqual(bad_password_form.errors['re_password'] , ['کلمه عبور باید حداقل 8 کاراکتر باشد'])

    def test_valid_emploee_register(self):
        valid_form = EmployeeRegister(data = self.valid_register )
        self.assertTrue(valid_form.is_valid())
