from django.test import TestCase
from Accounts.forms import RegisterForm
from Employer.models import Manager
from django.contrib.auth.models import User
from Tests.Employer.forms import TestEmployerForms
class TestAccountForms(TestCase):
    #setUp
    def setUp(self):
        User.objects.create_user('amin' ,'amin@gmail.com' ,'aminamin')
        Manager.objects.create(name = TestEmployerForms.valid_manager['name'] , family = TestEmployerForms.valid_manager['family'],
        email = TestEmployerForms.valid_manager['email'] , phone = '09182064916'
        )
        print(Manager.objects.get(phone = '09182064916'))

    def test_empty_register_form(self):
        form = RegisterForm(data = {})
        self.assertEqual(form.errors['name'] , ['نمیتواند خالی باشد'])

    def test_clean_methods(self):
        validform = RegisterForm(data = TestEmployerForms.valid_manager)
        unvalidform = RegisterForm(data = TestEmployerForms.unvalid_manager)
        # print(unvalidform.errors)
        # self.assertEqual(validform.errors['phone'] , ['این شماره قبلا در سایت ثبت شده است !'])
        # self.assertEqual(validform.errors['email'] , ['این ایمیل قبلا در سایت ثبت شده است !'])
        print(validform.errors)
        self.assertEqual(validform.errors['phone'] , ['شماره وارد شده صحیح نیست'])
        self.assertEqual(validform.errors['email'] , ['ایمیل وارد شده معتبر نیست.'])

    def test_valid_and_save(self):
        form = RegisterForm(data = TestEmployerForms.valid_manager)
        form.is_valid()
        user = form.save()
        self.assertIsInstance(user, Manager)
        self.assertTrue(form.is_valid())
