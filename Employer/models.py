import os
import django
from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()

from Controllers.models import soldiership_types , job_nature , categories, states_iran
from Controllers.utils import Advertisement_time_left

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
	profile_pic = models.ImageField(null = True,blank = True,default = 'static/images/company-2.jpg' ,upload_to = upload_image_path)
	email 		= models.EmailField(verbose_name = 'ایمیل')
	phone 		= models.CharField(max_length = 11 , verbose_name = 'شماره تلفن')
	About 		= models.TextField(verbose_name = 'درباره شما ' , default='متن معرفی کارفرما')

	def __str__(self):
		return self.email

def upload_logo_path(instance , filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.name}-{instance.id}-compnylogo{ext}"
    return f"company-logos/{final_name}"

class Company(models.Model):
	profile_pic = models.ImageField(null = True,blank = True,upload_to = upload_logo_path)
	name = models.CharField(max_length = 250 , verbose_name = 'نام شرکت')
	address = models.TextField(verbose_name = 'آدرس')
	underlie = models.TextField(verbose_name = 'درباره شرکت (این متن در آگهی های شما نمایش داده می شود)' , max_length = 2000)
	manager = models.ForeignKey(Manager , on_delete = models.CASCADE , related_name = 'Have_companies' , blank = True , null=True)
	valid = models.BooleanField(verbose_name = 'تایید کنید این شرکت وجود خارجی دارد' , default = False)

	def __str__(self):
		return self.name

class Advertisement(models.Model):
	title = models.CharField(max_length = 300 , verbose_name = 'عنوان آگهی')
	location = models.CharField(max_length = 100,choices=states_iran ,default = states_iran[0][0],verbose_name = 'شهر یا استان')
	address = models.TextField(verbose_name = 'آدرس' , blank=True , null = True)
	category = models.ForeignKey(categories , on_delete = models.CASCADE , default = '' , verbose_name = 'دسته بندی' , related_name = 'advertisiment')
	company = models.ForeignKey(Company , on_delete = models.CASCADE , verbose_name = 'مربوط به شرکت' , related_name='company' , null=True)
	text = models.TextField(verbose_name = 'متن آگهی')
	soldier_ship = models.CharField(max_length = 100, choices=soldiership_types , verbose_name = 'وضعیت خدمت کارجو')
	skills = models.TextField(verbose_name = 'مهارتهای مدنظر')
	job_nature = models.CharField(max_length = 30 , choices = job_nature , verbose_name = 'نوع قرارداد')
	generate_in = models.DateField(auto_now_add=True , verbose_name = 'تاریخ ایجاد',blank = True, null = True)
	expired_in = models.DateTimeField(verbose_name = 'تارخ انقضای این آگهی',blank = True, null = True)
	salary = models.IntegerField(verbose_name = 'حقوق (تومان)')

	expired = models.BooleanField(verbose_name = 'این آگهی منقضی شده' , default = False)

	def __str__(self):
		return self.title

	def get_time_left(self):
		return Advertisement_time_left(self)

applicant_status=(
('send' , 'در انتظار تأیین وضعیت'),
('seen' , 'توسط کارفرما مشاهده شد'),
('accepted' , 'تأیید برای مصاحبه'),
('rejected' , 'رد')
)

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name="applicants")
    created_at = models.DateTimeField(default=django.utils.timezone.now , verbose_name = 'تاریخ ارسال درخواست')
    seen_at = models.DateTimeField(null=True , verbose_name = 'مشاهده شده توسط کارفرما')
    determine_at = models.DateTimeField(null=True , verbose_name = 'تأیین وضعیت در تاریخ')
    status = models.CharField(max_length = 15 , choices = applicant_status , default = 'send')

hire_status = (
('waiting' , 'هنوز توسط کارجو مشاهده نشده'),
('seen' , 'مشاهده شده'),
('accepted','کارجو برای شما رزومه و اطلاعات تماس ارسال کرده است'),
('rejected' , 'توسط کارجو رد شده است')
)

class Hire(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE, blank = True , null = True , verbose_name = 'کاربر')
    text = models.TextField(verbose_name = 'متن پیشنهاد همکاری')
    contact = models.CharField(verbose_name = 'راه ارتباطی' , max_length = 200)
    ad   = models.ForeignKey(Advertisement ,null=True , on_delete = models.CASCADE , verbose_name = 'آگهی')
    status = models.CharField(choices = hire_status , default = 'waiting' , verbose_name = 'وضعیت' , max_length = 100)

class AdminMessage(models.Model):
	user = models.ManyToManyField(Manager , verbose_name = 'مدیر مورد نظر')
	title = models.CharField(max_length = 120 , verbose_name = 'موضوع')
	# message  = models.TextField(verbose_name = 'متن پیام')
	created_at = models.DateTimeField(auto_now_add = True)
	enable = models.BooleanField(default=True , verbose_name = 'توسط مدیر دیده شود')
	new = models.BooleanField(default=True)