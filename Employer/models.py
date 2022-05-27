import os
from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()

from Controllers.models import soldiership_types , job_nature , categories

from django.contrib.auth.models import User

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.name}-{instance.family}{ext}"
    return f"Manager-ProfilePics/{final_name}"

class Manager(models.Model):
	name 		= models.CharField(max_length = 100 , verbose_name = 'نام')
	family  	= models.CharField(max_length = 150 , verbose_name = 'نام خانوادگی')
	profile_pic = models.ImageField(null = True,blank = True,upload_to = upload_image_path)
	email 		= models.EmailField(verbose_name = 'ایمیل')
	phone 		= models.CharField(max_length = 11 , verbose_name = 'شماره تلفن')
	About 		= models.TextField(verbose_name = 'درباره شما ')

	def __str__(self):
		return self.name

def upload_logo_path(instance , filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.name}-{instance.id}-compnylogo{ext}"
    return f"company-logos/{final_name}"

class Company(models.Model):
	logo = models.ImageField(null = True,blank = True,upload_to = upload_logo_path)
	name = models.CharField(max_length = 250 , verbose_name = 'نام شرکت')
	address = models.TextField(verbose_name = 'آدرس')
	underlie = models.TextField(verbose_name = 'درباره شرکت (این متن در آگهی های شما نمایش داده می شود)')
<<<<<<< HEAD
	manager = models.ForeignKey(Manager , on_delete = models.CASCADE , default = 1 , related_name = 'Have_companies')
=======
	manager = models.ForeignKey(Manager , on_delete = models.CASCADE , default = 1)
>>>>>>> f1eee86f862167e6899b4c13b52add5a0b0166fa
	valid = models.BooleanField(verbose_name = 'تایید کنید این شرکت وجود خارجی دارد')

	def __str__(self):
		return self.name

class Advertisement(models.Model):
	title = models.CharField(max_length = 300 , verbose_name = 'عنوان آگهی')
	location = models.CharField(max_length = 100,verbose_name = 'شهر یا استان')
	category = models.ForeignKey(categories , on_delete = models.CASCADE , default = '' , verbose_name = 'دسته بندی' , related_name = 'advertisiment')
	company = models.ForeignKey(Company , on_delete = models.CASCADE , verbose_name = 'مربوط به شرکت' , related_name='company')
	text = models.TextField(verbose_name = 'متن آگهی')
	soldier_ship = models.CharField(max_length = 25, choices=soldiership_types , verbose_name = 'وضعیت خدمت کارجو')
	skills = models.TextField(verbose_name = 'مهارتهای مدنظر')
	job_nature = models.CharField(max_length = 30 , choices = job_nature , verbose_name = 'نوع قرارداد')
	generate_in = models.DateTimeField(auto_now_add=True , verbose_name = 'تاریخ ایجاد',blank = True, null = True)
	expired_in = models.DateTimeField(verbose_name = 'تارخ انقضای این آگهی',blank = True, null = True)
	salary = models.IntegerField(verbose_name = 'حقوق (تومان)')

	expired = models.BooleanField(verbose_name = 'این آگهی منقضی شده' , default = False)

	def __str__(self):

		return self.title

applicant_status=(
('send' , 'در انتظار تأیین وضعیت'),
('seen' , 'توسط کارفرما مشاهده شد'),
('accepted' , 'تأیید برای مصاحبه'),
('rejected' , 'رد شده')
)

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name="applicants")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length = 15 , choices = applicant_status , default = 'send')



