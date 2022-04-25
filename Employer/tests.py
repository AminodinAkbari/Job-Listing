from django.test import TestCase
from .forms import NewCompanyForm

from django.http import HttpRequest
from django.contrib.auth.models import User

# Create your tests here.
class TestNewCompanyForm(TestCase):
    def test_empty_form(self):
        form = NewCompanyForm()
        self.assertIn("name", form.fields)
        self.assertIn("address", form.fields)
        self.assertIn("underlie", form.fields)

    def test_form(self):
        user = User.objects.create_user(
            username="funny",
            email="just-for-testing@testing.com",
            password="dummy-insecure",
        )

        request = HttpRequest()
        request.POST = {
            "user": user.pk,
            "date": "2021-06-03",
            "due_date": "2021-06-03",
            "state": "UNPAID",
        }

        form = NewCompanyForm(request.POST)
        self.assertTrue(form.fields)