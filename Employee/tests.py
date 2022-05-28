from django.test import TestCase,Client
from Employee.models import EmployeeModel
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model




# Create your tests here.
class Test(TestCase):

	def setUp(self):
		User = get_user_model()
		User.objects.create_user('temporary')

	def test_update_employee(self):
		User = get_user_model()
		user = User.objects.get(username='temporary')
		obj = EmployeeModel.objects.create(employee = user)
		data = {
		'employee':obj.id,
		'profile_pic': ' ',
		'phone': '12345',
		'state': ' ',
		'address': ' ',
		'sex': ' ',
		'marital_status': ' ',
		'about_me': ' ',
		'skills': ' ',
		'birth': '1400/5/5',
		'employee_soldier_ship': ' ',
		'languages': ' ',
		'work_experience': ' ',
		'education': ' ',
		}
		response = self.client.post(reverse('UpdateResume' , kwargs={'pk':obj.id}) , data = data,enctype="multipart/form-data")
		self.assertEqual(response.status_code, 302)
		obj = EmployeeModel.objects.get(pk=user.id)
		print(obj.phone)
		# obj.refresh_from_db()
		# print(obj.phone)
		# self.assertEqual(obj.phone,'12345')
