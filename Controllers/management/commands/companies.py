from django.core.management.base import BaseCommand , CommandError
from Employer.models import Manager , Company
import random

company_names_list = ['Company Alpha' , 'Company Beta' , 'Company Charli' , 'Persian Company']
cities = ['تهران' , 'مشهد' , 'تبریز' , 'اصفهان' , 'همدان' , 'شیراز']

def make_underlie_text(arg):
    texts = [
    f'شرکت {arg} با هدف اعتلاء کارآفرینی و نوآوری در صنعت حفاظت الکترونیک و نظارت تصویری کشور، در سال 1376 تاسیس گردید و با پشتوانه بیش از 20 سال سابقه درخشان، هم اکنون بعنوان بزرگترین تولید کننده، واردات کننده و دارای گسترده ترین شبکه فروش و برترین شبکه خدمات از فروش در صنعت حفاظت الکترونیک ایران می باشد.' ,

    f' {arg} اولین و بزرگترین سامانه سفارش آنلاین غذا در ایران است. زودفود که در سال 1388 تاسیس شد، پس از ادغام به بدوفود و پیوستن به گروه ، کار خود را با نام {arg} ادامه داد.',

    f'شرکت بین المللی تولیدی و بازرگانی {arg}، ، فعالیت حرفه ای خود در حوزه ابزارالات را از سال 1381 آغاز کرده و هم اکنون بیش از 600 نفر به صورت مستقیم و بیش از 20000 نفر به صورت غیرمستقیم، در واحدهای تامین، ارتباطات و برند، انبار، خدمات پس از فروش، طرح و برنامه، دیجیتال مارکتینگ، زیر ساخت شبکه، منابع انسانی، صادرات، فروش محصولات و قطعات، مالی و حسابداری، و نرم افراز؛ مشغول خدمت رسانی به مصرف کنندگان هستند.'
    ]

    return random.choice(texts)

class Command(BaseCommand):
    def add_arguments(self , parser):
        parser.add_argument('Count' , type=int)

    def handle(self , *args , **options):
        name = random.choice(company_names_list) + str(random.randint(0 , 100))
        all_managers = Manager.objects.all()
        if len(all_managers) > 0:
            for i in range(0 , options['Count']):
                company = Company.objects.create(
                manager = (Manager.objects.order_by('?')[:1]).first(),
                name = name,
                address = str(random.choice(cities) + ' ، ' + 'خیابان ') + str(random.randint(1,10)) ,
                underlie = make_underlie_text(name),
                valid = True
                )

                self.stdout.write(self.style.SUCCESS(f'company {company.id} with name {company.name} created'))
        else:
            raise CommandError("You Should Have More Manager Model For Creating Companies")
