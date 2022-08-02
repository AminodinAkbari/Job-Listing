import random
from datetime import datetime, timedelta
today = datetime. today()

from django.core.management.base import BaseCommand , CommandError
from Employer.models import Company,Advertisement
from Controllers.models import categories , states_iran , employee_soldier_ship_types , job_nature

programing_languages = ['Python' , 'PHP' , 'C' , 'JAVA' , 'RUBY']

skills = [
['Python','Django','Django Rest Framwork'],
['PHP','Laravel','FastAPIs'],
['JAVA','Rest APIs'],
['C','FastAPIs','ASP.NET'],
['Ruby','Rubi On Railse'],
]

# states_iran = ['تهران' , 'گیلان' , 'اصفهان' , 'مشهد' , 'تبریز']

class Command(BaseCommand):
    def add_arguments(self , parser):
        parser.add_argument("category_id")
        parser.add_argument("Count" , type=int)

    def handle(self , *args , **options):
        try:
            category = categories.objects.get(id = options['category_id'])
        except:
            raise CommandError("ID Is'nt In DataBase")

        if len(Company.objects.all()) > 1 and category :
            for i in range(0 , options['Count']):

                skills_choiced = random.choice(skills)

                skills_final = ''
                for i in skills_choiced:
                    skills_final += str(i) + '/'

                Advertisement.objects.create(
                title = 'برنامه نویس ' + str(skills_choiced[0]),
                location = states_iran[random.randint(1,2)][1],
                category = category,
                company  = (Company.objects.order_by('?')[:1]).first(),
                text = 'قسمت تست متن آگهی میتواند به شما نشان دهد که ما دقیقا دنبال چه چیزی هستیم',
                soldier_ship = employee_soldier_ship_types[random.randint(0,4)][1],
                skills =skills_final ,
                job_nature = job_nature[random.randint(0,2)][random.randint(0,1)],
                expired_in = today + timedelta(days=60),
                salary = random.randint(1000000 , 10000000)
                )
        else:
            raise CommandError("Company Models Less Than 2 !")
