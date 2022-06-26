from django.test import TestCase,Client,RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from Employee.models import EmployeeModel
from Employee.forms import PersonalInfo_ResumeForm

c = Client()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user('amin','amin@gmail.com' , 'PaSs0wrd')
        
    def test_update_resume(self):
        user = User.objects.all().first()
        obj = EmployeeModel.objects.create(employee = user)
        response = self.client.post(
        reverse('UpdateResume' , kwargs = {'pk':obj.id}),
        {'birth':'2022-2-3'})
        self.assertEqual(response.status_code , 302)
