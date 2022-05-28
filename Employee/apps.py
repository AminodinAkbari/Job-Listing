from django.apps import AppConfig

class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Employee'
 
# class NewEmployee(AppConfig):
#     name = 'Employee'
#     def ready(self):
#         import Employee.signals
