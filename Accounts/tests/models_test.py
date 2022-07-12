from django.test import TestCase

from Accounts.models import Newsletter

class AccountsAppTest(TestCase):
    def test(self):
        print('♠ Testing Accounts.models.py')
        Newsletter.objects.create(email = 'Test@gmail.com')
        self.assertEqual(Newsletter.objects.all().first()._meta.get_field('email').max_length , 150)
        print('____________end_____________')
