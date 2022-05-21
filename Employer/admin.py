from django.contrib import admin
from .models import Manager , Company , Advertisement,Applicant

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'family' , 'phone']
	# exclude = ('password',)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'manager' , 'valid']

class AdAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'company' , 'category' , 'salary' , 'expired' ,'generate_in']

class ApplicantAdmin(admin.ModelAdmin):
	list_display = ['user' , 'ad' , 'created_at']
	
	def get_created_jalali(self, obj):
		return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

admin.site.register(Manager,ManagerAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Advertisement,AdAdmin)
admin.site.register(Applicant,ApplicantAdmin)