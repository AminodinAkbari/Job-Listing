from django.test import TestCase
from django.contrib.auth.models import User

from django.test import Client
from django.urls import reverse
# Create your tests here.

c = Client()
class TestAccount(TestCase):

	def __init__(self , *args , **kwargs):
		super(TestAccount , self).__init__(*args , **kwargs)
		global login_info , register_info
		login_info = {'username':'temporary' , 'password':'temporary'}
		register_info = {
		'name':'Amin' ,
		'family':'Akbari' ,
		'email':'test@test.com' ,
		'profile_pic':'static/images/bg_1.jpg',
		'phone':'09181234567' ,
		'password':'12345678' ,
		're_password':'12345678'
		}

	def setUp(self):
		user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

	def test_login_form(self):
		respone = c.post('/login',login_info)
		print(f'Status Code Is ♠{respone.status_code}♠')
		self.assertEquals(respone.status_code , 302)
		self.assertTrue(self.client.get(reverse('Login')))

	def test_logging_in(self):
		user = self.client.login(username = login_info['username'] , password = login_info['password'])
		self.assertTrue(user)

	def test_register_form(self):
		respone = c.post('/register' , register_info)
		print(f'Status Code Is ♠{respone.status_code}♠')
		self.assertEquals(respone.status_code , 302)
		self.assertTrue(self.client.get(reverse('Register')))

