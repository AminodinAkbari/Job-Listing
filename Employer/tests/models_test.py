from django.test import TestCase

from django.contrib.auth.models import User
from Employer import models
from Employee.models import EmployeeModel
from Controllers.models import categories,states_iran
from django.utils import timezone

class Employer_ModelsTest(TestCase):
    valid_manager= {
    'name':'amin',
    'family':'akbari',
    'phone' : '12345678901',
    'About' : 'test',
    'email' : 'user1@gmail.com',
    'password':'123456789' , 're_password' : '123456789',
    }

    valid_company = {
    'name' : 'test Company',
    'address' : 'test Address',
    'underlie' : 'For Example UnderLie',
    }

    valid_ad = {
    'title' : 'test title',
    'company' : models.Company.objects.all().first(),
    'category' : categories.objects.all().first(),
    'text' : 'Example For txt Advertisement',
    'soldier_ship' : 'passed',
    'skills' : 'test SKILLS',
    'job_nature' : 'FullTime',
    'salary' : 12000,
    }

    def setUp(self):
        User.objects.create_user(username = 'TestUser' , password = 'TestPassword')
        User.objects.create_user(username = 'TestEmployee' , password = 'TestPassword')
        EmployeeModel.objects.create(employee = User.objects.get(username = 'TestEmployee'))
        # Manager
        manager = models.Manager.objects.create(name = self.valid_manager['name'] , family = self.valid_manager['family'],
        phone = self.valid_manager['phone'] , About = self.valid_manager['About'] , email = self.valid_manager['email'],)
        self.client.login(username = 'user1@gmail.com' , password = 'PaSs0wrd')

        #company
        models.Company.objects.create(name = self.valid_company['name'] , address = self.valid_company['address'],
        underlie = self.valid_company['underlie'])

        #category
        categories.objects.create(name = 'Test Cate')

        #Advertisement
        models.Advertisement.objects.create(title = self.valid_ad['title'] , company = self.valid_ad['company'],
        category = categories.objects.all().first(),
        text = self.valid_ad['text'] , soldier_ship = self.valid_ad['soldier_ship'] , skills = self.valid_ad['skills'],
        job_nature = self.valid_ad['job_nature'] , salary = self.valid_ad['salary'])

    def test_Manager_Model(self):
        print(models.Manager.objects.all())
        manager = models.Manager.objects.get(id = 1)._meta
        self.assertEqual(manager.get_field('name').verbose_name , 'نام')
        self.assertEqual(manager.get_field('name').max_length , 100)
        self.assertEqual(manager.get_field('family').max_length , 150)
        self.assertEqual(manager.get_field('email').verbose_name , 'ایمیل')
        self.assertEqual(manager.get_field('phone').max_length , 11)
        self.assertEqual(manager.get_field('phone').verbose_name , 'شماره تلفن')
        self.assertEqual(manager.get_field('About').verbose_name , 'درباره شما ')

    def test_Company_Model(self):
        company = models.Company.objects.get(id = 1)._meta
        self.assertEqual(company.get_field('name').verbose_name , 'نام شرکت')
        self.assertEqual(company.get_field('name').max_length , 250)
        self.assertEqual(company.get_field('address').verbose_name , 'آدرس')
        self.assertEqual(company.get_field('underlie').verbose_name , 'درباره شرکت (این متن در آگهی های شما نمایش داده می شود)')
        self.assertEqual(company.get_field('underlie').max_length , 2000)

    def test_Advertisement_Model(self):
        Ad = models.Advertisement.objects.all().first()._meta

        self.assertEqual(Ad.get_field('title').max_length , 300)
        self.assertEqual(Ad.get_field('location').max_length , 100)
        self.assertEqual(Ad.get_field('soldier_ship').max_length , 100)
        self.assertEqual(Ad.get_field('job_nature').max_length , 30)
        self.assertEqual(Ad.get_field('location').choices , states_iran)
        self.assertEqual(Ad.get_field('category').default , '')
        self.assertTrue(Ad.get_field('generate_in').auto_now_add)
        self.assertFalse(Ad.get_field('expired').default)

    def test_Applicant_Model(self):
        models.Applicant.objects.create(employee = EmployeeModel.objects.all().first(),ad = models.Advertisement.objects.all().first())
        applicant = models.Applicant.objects.all().first()._meta
        self.assertEqual(applicant.get_field('status').max_length , 15)
        self.assertEqual(applicant.get_field('status').choices , models.applicant_status)
        self.assertEqual(applicant.get_field('created_at').default , timezone.now)

    valid_hire = {
    'user' : User.objects.all().first(),
    'text' : 'Example Text For text',
    'contact' : 'ABC',
    'ad' : models.Advertisement.objects.all().first(),
    }

    def test_Hire_Model(self):
        models.Hire.objects.create(user = self.valid_hire['user'],text = self.valid_hire['text'],
        contact = self.valid_hire['contact'] , ad = self.valid_hire['ad'])
        hire = models.Hire.objects.all().first()._meta
        self.assertEqual(hire.get_field('contact').max_length , 200)
        self.assertEqual(hire.get_field('status').max_length , 100)
        self.assertEqual(hire.get_field('status').choices , models.hire_status)
