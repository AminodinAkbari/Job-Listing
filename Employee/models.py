import os
# from jalali_date.fields import JalaliDateField
from django.db import models
from django.contrib.auth.models import User

from Controllers.models import (
employee_soldier_ship_types,
states_iran,
marital,
sex_types,
Languages,
)

from Employer.models import Advertisement

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"id-employee-{instance.employee.id}{ext}"
    return f"Employee-ProfilePics/{final_name}"

class EmployeeModel(models.Model):
	employee = models.ForeignKey(User , on_delete =models.CASCADE , related_name='employee' , blank=True , null = True)
	profile_pic = models.ImageField(null = True,blank = True,upload_to = upload_image_path)
	phone = models.CharField(max_length = 11 , verbose_name = 'تلفن', blank = True , null = True)
	state = models.CharField(max_length = 50 , choices = states_iran , verbose_name = 'استان محل سکونت' , blank = True , null = True)
	address = models.CharField(max_length = 200 , verbose_name = 'آدرس', blank = True , null = True)
	sex = models.CharField(max_length = 10 , choices=sex_types , verbose_name = 'جنسیت', blank = True , null = True)
	marital_status = models.CharField(max_length = 10 , choices=marital , verbose_name = 'وضعیت تأهل', blank = True , null = True)
	about_me = models.TextField(verbose_name = 'درباره من' , blank = True , null = True)
	skills = models.TextField(verbose_name = 'مهارت ها (مهارتهای خود را با "/ یا ،" از هم جدا کنید', blank = True , null = True)
	birth = models.DateField(blank=True , null=True)
	employee_soldier_ship = models.CharField(max_length = 25,choices=employee_soldier_ship_types , verbose_name = 'وضعیت نظام وظیفه (اگر خانم هستید نیاز به انتخاب گزینه نیست)', blank=True , null = True)
	languages = models.ManyToManyField(Languages , verbose_name = 'زبانهای گفتاری مسلط' , blank = True)
	work_experience = models.TextField(verbose_name = 'سوابق شغلی' , blank = True , null = True)
	education = models.TextField(verbose_name = 'تحصیلات', blank=True , null = True)

class Favorite(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	ad 	 = models.ForeignKey(Advertisement , on_delete = models.CASCADE , related_name = 'favortes_ads')
