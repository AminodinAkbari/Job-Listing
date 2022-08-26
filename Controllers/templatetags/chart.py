from django import template
register = template.Library()
from Controllers.models import states_iran 
from Employee.models import EmployeeModel

@register.inclusion_tag('employer-dashboard/states-chart.html' , takes_context=True)
def Chart(context):
	obj = EmployeeModel.objects.all().order_by('state')
	"""States Cart"""
	EN_list = []
	FA_list = []
	for i in states_iran[1:]:
		EN_list.append(i[0])
		FA_list.append(i[1])
	context['EN_list'] = list(EN_list)
	context['FA_list'] = list(FA_list)
	context['employees'] = obj

	"""Sex Chart"""
	all_empl = obj.count()
	if all_empl > 0:
		males = round(obj.filter(sex = 'Male').count() * 100 / all_empl)
		females = round(obj.filter(sex = 'Female').count() * 100 / all_empl)
		context['Males'] = males
		context['Females'] = females

	return context