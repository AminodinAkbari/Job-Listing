from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import EmployeeModel

@receiver(post_save , sender = User)
def create_employee_model(sender , instance , created , **kwargs):
	if created:
		EmployeeModel.objects.create(employee = instance)