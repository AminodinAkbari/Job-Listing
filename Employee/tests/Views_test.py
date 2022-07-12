from django.test import TestCase,Client,RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from Employee.models import EmployeeModel
from Employee.forms import PersonalInfo_ResumeForm

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user('amin','amin@gmail.com' , 'PaSs0wrd')
        obj = EmployeeModel.objects.create(employee = user)
        self.client.login(username = 'amin' , password = 'PaSs0wrd')

    def test_update_resume(self):
        employee = EmployeeModel.objects.get(employee_id = 1)
        response = self.client.get(reverse('UpdateResume' , kwargs = {'pk':employee.id}))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'Employee/CreateResume.html')

    def test_EditNameOrEmail_employee(self):
        response = self.client.get(reverse('EditNameOrEmail-Employee' , kwargs={'pk':1}))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employee/EditNameOrEmail-Employee.html')

        """Editing Username"""
        print('Changing Username')
        print('________')
        print(f'Before : {User.objects.get(id = 1).first_name}')
        print("♣POSTING DATA (first_name:Amin)♣")
        response = self.client.post(reverse('EditNameOrEmail-Employee' , kwargs={'pk':1}) , {'first_name':'Amin' , 'last_name':'akbari',
        'username':'amin@gmail.com' , 'email-name':True})
        print(f'After : {User.objects.get(id = 1).first_name}')
        print('________')
        User.objects.get(id = 1).first_name = ''

        """Editing Password"""
        print('Changing Password')
        print(f'Before : {User.objects.get(id = 1).password}')
        old = User.objects.get(id=1).password
        response = self.client.post(reverse('EditNameOrEmail-Employee' , kwargs={'pk':1}) , {'old':'PaSs0wrd' , 'new':'new_password',
        're_new':'new_password' , 'change-password':True})
        new = User.objects.get(id=1).password
        print(f'After : {User.objects.get(id = 1).password}')
        self.assertTrue(old!=new)

    def test_ApplicantDetail(self):
        response = self.client.get(reverse('ApplicantDetail' , kwargs = {'pk':1}))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employee/Applicant-detail.html')

    def test_EmployeeJobApply(self):
        response = self.client.get(reverse('EmployeeJobApply'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employee/EditNameOrEmail-Employee.html')

    def test_EmployeeJobMarked(self):
        response = self.client.get(reverse('AdsSaved'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employee/employee-AdsMarked.html')

    def test_HireList(self):
        response = self.client.get(reverse('HiresList'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employee/Hire-messages.html')
