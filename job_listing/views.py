from django.shortcuts import render

from Employer.models import Manager,Advertisement

def Index(request):
	context = {}

	if request.user.is_authenticated:
		is_a_manager = Manager.objects.filter(email = request.user.username).exists()
		context['is_a_manager'] = is_a_manager

		is_a_employee = None
		
	return render(request , 'index.html' , context)