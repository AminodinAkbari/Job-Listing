from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()

from Controllers.models import soldiership_types , job_nature , categories

# Create your models here.
class Manager(models.Model):
	name 		= models.CharField(max_length = 100 , verbose_name = 'نام')
	family  	= models.CharField(max_length = 150 , verbose_name = 'نام خانوادگی')
	profile_pic = models.ImageField(null = True,blank = True,upload_to = 'Managers-ProfilePics')
	email 		= models.EmailField(verbose_name = 'ایمیل')
	phone 		= models.CharField(max_length = 11 , verbose_name = 'شماره تلفن')
	# password= models.CharField(max_length = 100)

	def __str__(self):
		return self.name


class Company(models.Model):
	name = models.CharField(max_length = 250 , verbose_name = 'نام شرکت')
	address = models.TextField(verbose_name = 'آدرس')
	underlie = models.TextField(verbose_name = 'درباره شرکت (این متن در آگهی های شما نمایش داده می شود)')
	manager = models.ForeignKey(Manager , on_delete = models.CASCADE , default = 1)
	valid = models.BooleanField(verbose_name = 'تایید کنید این شرکت وجود خارجی دارد')

	def __str__(self):
		return self.name

class Advertisement(models.Model):
	title = models.CharField(max_length = 300 , verbose_name = 'عنوان آگهی')
	location = models.CharField(max_length = 100,verbose_name = 'شهر یا استان')
	category = models.ForeignKey(categories , on_delete = models.CASCADE , default = '' , verbose_name = 'دسته بندی')
	company = models.ForeignKey(Company , on_delete = models.CASCADE , verbose_name = 'مربوط به شرکت')
	text = models.TextField(verbose_name = 'متن آگهی')
	soldier_ship = models.CharField(max_length = 25, choices=soldiership_types , verbose_name = 'وضعیت خدمت کارجو')
	skills = models.TextField(verbose_name = 'مهارتهای مدنظر')
	job_nature = models.CharField(max_length = 30 , choices = job_nature , verbose_name = 'نوع قرارداد')
	generate_in = models.DateTimeField(auto_now_add=True , verbose_name = 'تاریخ ایجاد')
	expired_in = models.DateField(verbose_name = 'تارخ انقضای این آگهی')
	salary = models.IntegerField(verbose_name = 'حقوق (تومان)')

	expired = models.BooleanField(verbose_name = 'این آگهی منقضی شده' , default = False)


	def __str__(self):

		return self.title
