from django.core.management.base import BaseCommand , CommandError
from Controllers.models import categories
import random

categories_names_list = ['خدمات پزشکی' , 'هنر' , 'گرافیک']

class Command(BaseCommand):
    def add_arguments(self , parser):
        parser.add_argument("Count" , type = int)

    def handle(self , *args , **options):

        all_categories = categories.objects.all()
        all_categories_list = []
        used_items = []

        for item in all_categories:
            all_categories_list.append(item.name)

        categories_count = options['Count']
        for make in range(0 , categories_count):
            name = random.choice(categories_names_list)

            if name not in all_categories_list and name not in used_items:
                categories.objects.create(name=name)
                self.stdout.write("Member Created !")
                used_items.append(name)
