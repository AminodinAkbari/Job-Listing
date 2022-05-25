from django.shortcuts import redirect
from Employer.models import Manager
from Employee.models import EmployeeModel
from django.core.exceptions import ValidationError
# Create your views here.
def Who_is(func):
	def wrapper(request,*args , **kwargs):
		try:
			manager = Manager.objects.get(email = request.user.username)
		except:
			manager = None
		return func(request,*args , **kwargs , user_type = manager)
	return wrapper


def employee_owner_can_access(func):
	def wrapper(request ,pk , *args , **kwargs):
		try:
			employee = EmployeeModel.objects.filter(employee = pk).first()
		except:
			employee = None
			return redirect('/')

		if employee is not None:
			if employee.employee != request.user:
				return redirect('/')
			
		return func(request , pk ,*args , **kwargs , employee = employee)
	return wrapper

def file_size(value): # add this to some file where you can import it from
	limit = 2 * 1024 * 1024
	if value.size > limit:
		raise ValidationError('حجم تصویر زیاد است ! اندازه فایل نباید بالای 2مگابایت باشد')

