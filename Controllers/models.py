#models include the some options in other models . for example choices for job_natuer in Employer models , kept here.

from django.db import models

# Create your models here.

soldiership_types = (
('passed' , 'کارت پایان خدمت یا معافیت دائم'),
('temporary' , 'معافیت تحصیلی'),
('other' , 'مهم نیست')
)

job_nature = (
('FullTime' , 'تمام وقت'),
('PartTime' , 'نیمه وقت'),
('Remote' , 'دورکاری')
)

class categories(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name