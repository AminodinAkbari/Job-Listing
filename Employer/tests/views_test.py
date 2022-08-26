from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User

from Employer.models import Manager

class BaseTest(TestCase):

    valid_manager= {
    'name':'amin',
    'family':'akbari',
    'phone' : '12345678901',
    'About' : 'test',
    'email' : 'user1@gmail.com',
    'password':'123456789' , 're_password' : '123456789',
    }
    valid_manager2= {
    'name':'ahmad',
    'family':'mohammadi',
    'phone' : '12345678900',
    'About' : 'test',
    'email' : 'user2@gmail.com',
    'password':'123456789' , 're_password' : '123456789',
    }

    def setUp(self):
        user = User.objects.create_user(username = 'user1@gmail.com' , password='PaSs0wrd')
        user2 = User.objects.create_user(username = 'user2@gmail.com' , password='PaSs0wrd')

        manager1 = Manager.objects.create(name = self.valid_manager['name'] , family = self.valid_manager['family'],
        phone = self.valid_manager['phone'] , About = self.valid_manager['About'] , email = self.valid_manager['email'],)
        self.client.login(username = 'user1@gmail.com' , password = 'PaSs0wrd') #.id = 1

        manager2 = Manager.objects.create(name = self.valid_manager2['name'] , family = self.valid_manager2['family'],
        phone = self.valid_manager2['phone'] , About = self.valid_manager2['About'] , email = self.valid_manager2['email'],)
        # self.client.login(username = 'user2@gmail.com' , password = 'PaSs0wrd') #.id = 2


    def test_manager_panel(self):
        self.client.logout()
        """Try Access Another Panel (username != Manager.email)"""
        self.client.login(username = 'user2@gmail.com' , password = 'PaSs0wrd')
        false_response = self.client.get(reverse('ManagerPanel',kwargs = {'pk':1}))
        self.assertEqual(false_response.status_code , 302)
        self.assertURLEqual(reverse('Home') , '/')
        self.client.logout()

        """Correct Manager Try Access Own Panel"""
        self.client.login(username = 'user1@gmail.com' , password = 'PaSs0wrd')
        True_response = self.client.get(reverse('ManagerPanel',kwargs = {'pk':1}))
        self.assertEqual(True_response.status_code , 200)
        self.assertTemplateUsed('employer-dashboard/ManagerPanel.html')
        self.assertURLEqual(reverse('ManagerPanel' , kwargs = {'pk':Manager.objects.all().first().id}) , '/manager_panel/1')
        # self.client.logout()

    def test_EditAdView(self):
        response = self.client.get(reverse('EditAdView',kwargs = {'pk':Manager.objects.all().first().id}))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employer/EditAdInfo.html')
        self.assertURLEqual(reverse('EditAdView' , kwargs = {'pk':Manager.objects.all().first().id}) , '/editad_view/1')

    def test_UpdatePasswordAndEmail_Manager(self):
        response = self.client.get(reverse('UpdatePasswordManager'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employer/UpdateManagersPassword.html')
        self.assertURLEqual(reverse('UpdatePasswordManager') , '/update_manager_password')

        """Editing Username"""
        print('Changing Username')
        print('________')
        print(f'Before : {User.objects.get(id = 1).username}')
        print("♣POSTING DATA (email = edited@gmail.com)♣")
        response = self.client.post(reverse('UpdatePasswordManager') , {'email':'edited@gmail.com' , 'update-email':True})
        print(f'After : {User.objects.get(id = 1).username}')
        print('________')
        self.client.post(reverse('UpdatePasswordManager') , {'email':'user1@gmail.com' , 'update-email':True})

        """Editing Password"""
        print('Changing Password')
        print(f'Before : {User.objects.get(id = 1).password}')
        old = User.objects.get(id=1).password
        response = self.client.post(reverse('UpdatePasswordManager') , {'old_password':'PaSs0wrd' , 'new_password':'new_password',
        're_new_password':'new_password' , 'update-pass':True})
        new = User.objects.get(id=1).password
        print(f'After : {User.objects.get(id = 1).password}')
        self.assertTrue(old!=new)

        """Undo Password And Re-Login"""
        response = self.client.post(reverse('UpdatePasswordManager') , {'old_password':'new_password' , 'new_password':'PaSs0wrd',
        're_new_password':'PaSs0wrd' , 'update-pass':True})

    def test_NewAd(self):
        response = self.client.get(reverse('NewAd'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employer/New_Ad.html')

    def test_NewCompany(self):
        response = self.client.get(reverse('NewCompany'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employer/New_company.html')

    def test_EditCompanyView(self):
        response = self.client.get(reverse('EditCompanyView' , kwargs={'pk':1}))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employer/EditCompanyInfo.html')

    def test_employee_apply_determine(self):
        response = self.client.get(reverse('DetermineTheStatus' , kwargs = {'pk':1 , 'adver_id':1}))
        self.assertTemplateUsed('Employer/EmployeeDetermine.html')
        self.assertEqual(response.status_code , 200)

    def test_NewHire(self):
        response = self.client.get(reverse('NewHire' , kwargs={'employee_id':1}))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed('Employer/NewHire.html')
