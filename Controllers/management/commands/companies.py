from django.core.management.base import BaseCommand , CommandError
from Employer.models import Manager , Company
import random

company_names_list = ['Company Alpha' , 'Company Beta' , 'Company Charli' , 'Persian Company']

class Command(BaseCommand):
    def add_arguments(self , parser):
        parser.add_argument('Count' , type=int)

    def handle(self , *args , **options):
        all_managers = Manager.objects.all()
        if len(all_managers) > 0:
            for i in range(0 , options['Count']):
                company = Company.objects.create(
                manager = (Manager.objects.order_by('?')[:1]).first(),
                name = random.choice(company_names_list) + str(random.randint(0 , 100)),
                address = 'تهران ، خیابان 15 ، جنب کوچه شهرداری منطقه 4' ,
                underlie = 'این شرکت یک شرکت استارتاپی فعال در حوزه هوش مصنوعی و توسعه وب می باشد',
                valid = True
                )

                self.stdout.write(self.style.SUCCESS(f'company {company.id} with name {company.name} created'))
                # self.sdout.write('Now You Can Run "" ')
        else:
            raise CommandError("You Should Have More Manager Model For Creating Companies")
