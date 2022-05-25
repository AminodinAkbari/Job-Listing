from django.contrib import admin
from Employee.models import EmployeeModel , Favorite
# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ['employee' , 'phone' , 'birth']
admin.site.register(EmployeeModel , EmployeeModelAdmin)
admin.site.register(Favorite)