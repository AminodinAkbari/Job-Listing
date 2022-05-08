from django.shortcuts import render
from Employer.models import Manager
# Create your views here.
def Who_is(func):
	def wrapper(request,*args , **kwargs):
		try:
			manager = Manager.objects.get(email = request.user.username)
		except:
			manager = None
		return func(request,*args , **kwargs , user_type = manager)
	return wrapper


