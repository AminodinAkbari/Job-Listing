from django import template
from Employer.models import Manager
from Employee.models import EmployeeModel
register = template.Library()

@register.inclusion_tag('BASE_HTMLs/Nav.html' , takes_context=True)
def Navbar(context , request):
	try:
		is_a_manager = Manager.objects.get(email = request.user.username) 
	except:
		is_a_manager = None

	try:
		is_a_employee = EmployeeModel.objects.get(employee = request.user)
	except:
		is_a_employee = None

	context = {}
	if request.user.is_authenticated:
		context['is_a_manager'] = is_a_manager
		context['is_a_employee'] = is_a_employee 
		context['request'] = request

	return context