from django.core.management.base import BaseCommand , CommandError
from Controllers.models import categories
import random

categories_names_list = ['خدمات' , 'حمل و نقل' , 'تولید محتوا' , 'آموزش' , 'حساب داری و مالی',
'مدیریتی' , 'صنایع و تولید' , 'تعمیرات']

class Command(BaseCommand):
    help = f"In This Command You Can Make {len(categories_names_list)} Categories !"
    def add_arguments(self , parser):
        parser.add_argument("Count" , type = int)

    def handle(self , *args , **options):
        if options['Count'] <= len(categories_names_list):
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
                    self.stdout.write(f"category {name} Created !")
                    used_items.append(name)
        else:
            raise CommandError(f'Count Should Smaller Or Equal To {len(categories_names_list)}')
