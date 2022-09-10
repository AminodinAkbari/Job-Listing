import random
from django.core.management.base import BaseCommand , CommandError

from django.contrib.auth.models import User
from Employer.models import Manager

first_name_example = ['علیرضا','حمید' ,'امیر' , 'امین' , 'رضا' , 'امید' , 'محمد' ]
last_name_example  = ['اکبری' , 'محمدی' , 'حیدری' , 'موسوی']
numbers = ['1','2','3','4','5','6','7','8','9','0']

def phone_number(arg):
    my_list = random.choices(arg , k=11)
    str1=''
    make_phone_number = str1.join(my_list)
    return make_phone_number

class Command(BaseCommand):
    help = "With This Command You Can Make Random Managers , Any Count You Want !"
    def add_arguments(self , parser):
        parser.add_argument("make-some-managers" , type=str)
        parser.add_argument("Count" , type=int)

    def handle(self ,*args, **options):

        random_name = random.choice(first_name_example)
        random_family = random.choice(last_name_example)

        for i in range(0 , options['Count']):
            choiced = 'example' + str(random.choice(range(0 , 1000))) + '@gmail.com'

            user = User.objects.create_user(
            username=choiced,
            password = '123456789',
            first_name = random_name,
            last_name = random_family,
            )

            manager = Manager.objects.create(
            name = random_name,
            family = random_family,
            email = choiced,
            phone = phone_number(numbers),
            About = f'سلام من {random_name} {random_family} هستم ، مدیر چند شرکت بزرگ و با این متن کوتاه قسمت معرفی خودم رو پر میکنم'
            )

            print(f'Manager {manager.id} And User {user.id} created')
        self.stdout.write(self.style.SUCCESS('Now You Can Run "companies count" command '))
