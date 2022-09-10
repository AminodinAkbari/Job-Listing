#models include the some options in other models . for example choices for job_natuer in Employer models , kept here.

from django.db import models
import string
import random

from django.db import reset_queries
import datetime
from django.db import connection

from django.shortcuts import redirect
# Create your models here.

soldiership_types = (
('passed' , 'کارت پایان خدمت یا معافیت دائم'),
('temporary' , 'معافیت تحصیلی'),
('other' , 'مهم نیست')
)

employee_soldier_ship_types = (
('A' , 'کارت پایان خدمت'),
('B' , 'معافیت تحصیلی'),
('C' , 'معافیت دائم'),
('D' , 'مشمول'),
('Shes a Woman' , 'شامل من نیست (مختص خانم ها)')
)

job_nature = (
('FullTime' , 'تمام وقت'),
('PartTime' , 'نیمه وقت'),
('Remote' , 'دورکاری')
)

# states_iran = (
# ('0' , 'استان مورد نظر'),
# ('Tehran' , 'تهران'),
# ('Shiraz' , 'شیراز'),
# ('Esfahan' , 'اصفهان'),
# ('Mashhad' , 'مشهد'),
# ('Tabriz' , 'تبریز'),
# ('Hamedan' , 'همدان'),
# ('Mazandaran' , 'مازندران'),
# ('Gilan' , 'گیلان'),
# ('Qom' , 'قم'),
# ('Markazi' , 'مرکزی'),
# )

marital = (
('Married','متأهل'),
('Single' , 'مجرد'),
)

sex_types = (
('Male','مرد') ,
('Female' , 'زن'),
)

class Languages(models.Model):
    lang_fa_type = models.CharField(max_length = 30)
    lang_en_type = models.CharField(max_length = 30)

    def __str__(self):
        return self.lang_fa_type

class categories(models.Model):
    name = models.CharField(max_length = 100)
    icon = models.CharField(max_length = 80 , blank=True , null=True)

    def __str__(self):
        return self.name

class states_iran(models.Model):
    name = models.CharField(max_length = 80 , verbose_name='نام استان')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

def passGenerator(passlen):
      main_password=string.ascii_letters+string.digits+"!@#$%^&*_+\/~"
      passwordlist=[]
      for i in range(passlen):
            passRandom=random.choice(main_password)
            passwordlist.append(passRandom)
      finalPass="".join(passwordlist)
      return finalPass


def debugger(func):
    def wrapper(*args,**kwargs):
        reset_queries()
        start_time = datetime.time()
        value = func(*args,**kwargs)
        end_time = datetime.time()
        queries = len(connection.queries)
        print(f"\n-------------\nConection Numbers: {queries} \n taketime = {(end_time):.3f}\n-----------\n")
        return value
    return wrapper
