from django.core.management.base import BaseCommand
from .iran_state import list
from Controllers.models import states_iran
class Command(BaseCommand):
	def add_arguments(self , parser):
		pass

	def handle(self , *args , **options):
		for i in list:
			creating = states_iran.objects.create(name = i.get('name'))
			print(f'province number {creating.id} created .')

		print(f'{len(states_iran.objects.all())} Successfuly Created .')
