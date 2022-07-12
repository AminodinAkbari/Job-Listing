from django.test import TestCase

from django.contrib.auth.models import User
from Employee import models

class BaseTest(TestCase):
    def setUp(self):
        User.objects.create_user(username = 'TestUser' , password = 'Password')
        models.EmployeeModel.objects.create(employee = User.objects.all().first())

    def test_EmployeeModel(self):
        employee_model = models.EmployeeModel.objects.all().first()._meta
        for i in employee_model.get_fields():
            if i != employee_model.get_field('id') and i != employee_model.get_field('languages'):
                self.assertEqual(i.null , True)

    def test_Favorite_Model(self):
        """ No Need To Test """
        pass
