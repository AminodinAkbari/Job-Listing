from django.test import TestCase
from Employer.forms import (
EditManagerInfoForm ,
EditEmailEmployer ,
UpdatePasswordManagersForm ,
NewAdvertisementForm ,
NewCompanyForm ,
EditAdInfoForm ,
)
from Employer.models import Manager , Company , categories , Advertisement
from django.contrib.auth.models import User
from django.http import HttpResponse
response = HttpResponse()

class TestEmployerForms(TestCase):

    valid_manager= {
    'name':'amin',
    'family':'akbari',
    'phone' : '12345678901',
    'About' : 'test',
    'email' : 'temp@gmail.com',
    }

    unvalid_manager= {
    'name':'amin',
    'family':'akbari',
    'phone' : '09182061234',
    'About' : 'test',
    'email' : 'amin@gmail.com',
    }

    no_duplicate_info = {
    'name':'test',
    'family':'test',
    'phone' : '09182061212',
    'About' : 'test',
    'email' : 'Test@gmail.com',
    }

    all_passwords_error = {
    'old_password' : '123' ,
    'new_password' : '123',
    're_new_password' : '1234'
    }

    char_30 = {'char_30':'123456789101112131415161718192'}

    valid_ad = {
    'title' : 'test 5 char title',
    'location' : 'Tehran',
    'category' : categories.objects.all().first(),
    'company' : Company.objects.all().first() ,
    'text' : char_30 ,
    'soldier_ship' : 'passed',
    'skills' : '1/2/3',
    'job_nature' : 'Remote',
    'expired_in':'1380-3-2',
    'salary' : 12000 ,

    }
    invalid_ad = {
    'title' : '1234',
    'location' : 'Tehran',
    'category' : categories.objects.all().first(),
    'company' : Company.objects.all().first() ,
    'text' : 'too short' ,
    'soldier_ship' : 'passed',
    'skills' : '1',
    'job_nature' : '' ,
    'expired_in':'1380-3-2',
    'salary' : 12000 ,
    }

    valid_company = {
    'name' : 'test' ,
    'address' : 'test street' ,
    'underlie' : 'test text for underlie' ,
    'manager' : Manager.objects.all().first(),
    }

    def setUp(self):
        self.user = User.objects.create_user('amin@gmail.com' ,'amin@gmail.com' ,'aminamin')
        manager1=Manager.objects.create(name = self.valid_manager['name'] , family = self.valid_manager['family'],
        email = self.unvalid_manager['email'] , phone = self.valid_manager['phone']
        )
        manager2=Manager.objects.create(name = self.valid_manager['name'] , family = self.valid_manager['family'],
        email = self.valid_manager['email'] , phone = self.unvalid_manager['phone']
        )
        company1 = Company.objects.create(name = 'test' , address = 'test street' , underlie = 'test' , manager = manager1 , valid = True)
        category1 = categories.objects.create(name = 'category1')

    def test_edit_info_empty_form(self):
        form = EditManagerInfoForm(data = {})
        self.assertEqual(form.errors['name'] , ['نمیتواند خالی باشد'])
        self.assertEqual(form.errors['family'] , ['نمیتواند خالی باشد'])
        self.assertEqual(form.errors['phone'] , ['نمیتواند خالی باشد'])

    def test_edit_info_duplicate_and_invalid_phone(self):
        duplicate_phone = EditManagerInfoForm(data = {'phone' : self.valid_manager['phone']})
        unvalid_phone   = EditManagerInfoForm(data = {'phone' : '123'})
        self.assertEqual(unvalid_phone.errors['phone'] , ['شماره تلفن نا معتبر است'])
        self.assertEqual(duplicate_phone.errors['phone'] , ['این شماره قبلا استفاده شده'])

    def test_edit_info_invalid_and_duplicate_email(self):
        invalid_email = EditEmailEmployer(data = {'email' : 'badmail'} , user = self.user)
        duplicate_email = EditEmailEmployer(data = {'email' : self.valid_manager['email']} , user=self.user)
        self.assertEqual(invalid_email.errors['email'] , ['ایمیل معتبر نیست'])
        self.assertEqual(duplicate_email.errors['email'] , ['این ایمیل قبلا استفاده شده است'])

    def test_valid_edit_info_managers_form(self):
        form = EditManagerInfoForm(data = self.no_duplicate_info)
        self.assertTrue(form.is_valid())

#------------ Change Password Form -----------------
    # correct password but same with new_password
    def test_same_old_pass_and_new_pass(self):
        form_same_OldandNew = UpdatePasswordManagersForm(data = {'old_password':'aminamin' , 'new_password' : 'aminamin'} , user = self.user)
        self.assertEqual(form_same_OldandNew.errors['new_password'] , ['مقادیر رمز عبور جدید با رمز عبور قبلی نمی‌تواند یکی باشد'])
        self.assertEqual(form_same_OldandNew.errors['re_new_password'] , ['نمیتواند خالی باشد'])

    # wrong password and short new_password
    def test_wrong_password_and_short_new_password(self):
        form = UpdatePasswordManagersForm(data = {'old_password' : 'wrong' , 'new_password' : 'short'} , user=self.user)
        self.assertEqual(form.errors['old_password'] , ['رمز عبور حال حاضر اشتباه می‌باشد'])
        self.assertEqual(form.errors['new_password'] , ['کلمه عبور باید حداقل 8 کاراکتر باشد'])

    # correct password and set a new password but re_new is wrong
    def test_wrong_password_repeat(self):
        form = UpdatePasswordManagersForm(
        data = {'old_password' : 'aminamin' ,'new_password' : 'new_pass_for_amin' ,'re_new_password' : 'wrong_repeat!'} , user=self.user)
        self.assertEqual(form.errors['re_new_password'] , ['کلمه های عبور با یکدیگر مغایرت دارند !'])

    def test_all_password_fields_required(self):
        form = UpdatePasswordManagersForm(data = {} ,user = self.user)
        self.assertEqual(form.errors['old_password'] , ['نمیتواند خالی باشد'])
        self.assertEqual(form.errors['new_password'] , ['نمیتواند خالی باشد'])
        self.assertEqual(form.errors['re_new_password'] , ['نمیتواند خالی باشد'])

# --------------- New and Edit Advertisement ------------------------
    def test_empty_form_new_advertisement(self):
        form = NewAdvertisementForm(data = {},user = self.user)
        # first field is :
        self.assertEqual(form.errors['title'] , ['نمی‌تواند خالی باشد'])
        # last field is :
        self.assertEqual(form.errors['salary'] , ['نمی‌تواند خالی باشد'])

    def test_clean_methods_new_ad_form(self):
        form = NewAdvertisementForm(data={'title':'short','skills':'one' , 'text':'short text'})
        self.assertEqual(form.errors['title'] , ['لطفا عنوان بهتری برای آگهی ایجادکنید (عنوان بسیار کوتاه است)'])
        self.assertEqual(form.errors['text'] , ['توضیحات این آگهی نمیتواند بسیار کوتاه باشد'])
        self.assertEqual(form.errors['skills'] , ['برای شفاف بودن آگهی ، لطفا حداقل 3 مهارت اضافه کنید'])

    def test_valid_new_ad(self):
        form = NewAdvertisementForm(data = self.valid_ad , user = self.user)
        created = form.save()
        self.assertTrue(form.is_valid())
        self.assertIsInstance(created , Advertisement)

    def test_EditAdInfoForm_empty_fields(self):
        form = EditAdInfoForm(data = {})
        # first field is :
        self.assertEqual(form.errors['title'] , ['نمی‌تواند خالی باشد'])
        # last field is :
        self.assertEqual(form.errors['salary'] , ['نمی‌تواند خالی باشد'])

    def test_clean_methods_EditAdInfoForm(self):
        form = EditAdInfoForm(data=self.invalid_ad)
        self.assertEqual(form.errors['job_nature'],['نمی‌تواند خالی باشد'])
        self.assertEqual(form.errors['skills'] , ['برای شفافیت آگهی ، باید حداقل 2 مهارت اضافه کنید.'])
        self.assertEqual(form.errors['text'] , ['توضیحات این آگهی نمیتواند بسیار کوتاه باشد'])
        self.assertEqual(form.errors['title'] , ['لطفا عنوان بهتری برای آگهی ایجادکنید (عنوان بسیار کوتاه است)'])

    def test_valid_EditAdInfoForm(self):
        form = EditAdInfoForm(initial = self.valid_ad , data = self.valid_ad)
        self.assertTrue(form.is_valid())

#----------------------New Company Form-----------------------------

    def test_empty_fields_new_company(self):
        form = NewCompanyForm(data = {})
        self.assertEqual(form.errors['name'] , ['نمی‌تواند خالی باشد'])
        self.assertEqual(form.errors['address'] , ['نمی‌تواند خالی باشد'])
        self.assertEqual(form.errors['underlie'] , ['نمی‌تواند خالی باشد'])

    def test_NewCompanyForm(self):
        form = NewCompanyForm(data = self.valid_company)
        created = form.save()
        self.assertTrue(form.is_valid())
        self.assertIsInstance(created , Company)

#------------------ Hire Form -----------------
