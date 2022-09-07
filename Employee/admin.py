from django.contrib import admin
from Employee.models import EmployeeModel
# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ['employee' , 'phone']
admin.site.register(EmployeeModel , EmployeeModelAdmin)