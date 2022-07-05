from django.test import TestCase
from django.contrib.auth.models import User
from Employee.models import EmployeeModel
from django.urls import reverse

valid_Employer = {
'name' : 'Amin',
'family' : 'Akbari',
'email' : 'amin@gmail.com',
'phone' : '09182064916',
'About' : 'Test',
'password' : '123456789',
're_password' : '123456789',
}

class BaseTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username = 'test@gmail.com' , password = 'ami123.789')
        EmployeeModel.objects.create(employee = user)
        self.response = self.client.get(reverse('Login'))

    def test_login_view(self):
        response = self.client.get(reverse('Login') , follow=True)
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , "Accounts/login.html")
        login = self.client.post(reverse('Login') , {'username':'test@gmail.com' , 'password':'ami123.789'})
        self.assertEqual(login.status_code , 302)

    def test_login_if_user_already_logged_in(self):
        self.client.login(username = 'test@gmail.com' , password = 'ami123.789')
        response = self.client.get(reverse('Login'))
        self.assertURLEqual(reverse('Home') , '/')
        self.client.logout()

    def test_Employers_register(self):
        response = self.client.get(reverse('Register'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'Accounts/register.html')
