from django.contrib import admin
from Employer import models

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'email' ,'family' , 'phone']
	# exclude = ('password',)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'manager' , 'valid']

class AdAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'company' , 'category' , 'salary' , 'expired' ,'generate_in']

class ApplicantAdmin(admin.ModelAdmin):
	# list_display = ['employee' , 'ad' , 'created_at']
	pass

	def get_created_jalali(self, obj):
		return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

class HireAdmin(admin.ModelAdmin):
	list_display = ['user' , 'ad' , 'status']

admin.site.register(models.Manager,ManagerAdmin)
admin.site.register(models.Company,CompanyAdmin)
admin.site.register(models.Advertisement,AdAdmin)
admin.site.register(models.Applicant,ApplicantAdmin)
admin.site.register(models.Hire,HireAdmin)
admin.site.register(models.Favorite)
# admin.site.register(models.AdminMessage)
