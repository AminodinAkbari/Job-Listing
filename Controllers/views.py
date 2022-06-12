from django.shortcuts import redirect, render
from Employer.models import Manager , Advertisement , Applicant
from Employee.models import EmployeeModel

from django.core.exceptions import ValidationError
from django.views.generic import ListView

from .forms import SearchForm

from django.utils import timezone
now = timezone.now()

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

def file_size(value):
	limit = 2 * 1024 * 1024
	if value.size > limit:
		raise ValidationError('حجم تصویر زیاد است ! اندازه فایل نباید بالای 2مگابایت باشد')

def is_valid_queryparam(param):
    return param != '' and param is not None

def search_filter(request):
	obj = Advertisement.objects.filter(expired_in__gt = now)
	category = request.GET.get('category')
	location = request.GET.get('location')
	title = request.GET.get('title')
	job_nature = request.GET.get('job_nature')

	if is_valid_queryparam(title):
		obj = obj.filter(title__icontains = title)

	if is_valid_queryparam(location):
		obj = obj.filter(location__iexact = location)

	if is_valid_queryparam(category):
		obj = obj.filter(category__name__iexact = category)

	if is_valid_queryparam(job_nature):
		obj = obj.filter(job_nature__iexact = job_nature)

	if is_valid_queryparam(category) and is_valid_queryparam(title) and is_valid_queryparam(location):
		obj = obj.filter(category__name__iexact = category , title__icontains = title , location__icontains = location )

	if is_valid_queryparam(category) and is_valid_queryparam(title):
		obj = obj.filter(category__name__iexact = category , title__icontains = title)

	if is_valid_queryparam(category) and is_valid_queryparam(location):
		obj = obj.filter(category__name__iexact = category , location__iexact = location)

	if is_valid_queryparam(title) and is_valid_queryparam(location):
		obj = obj.filter(title__icontains = title , location__iexact = location)

	return obj

def search_employee(request):
	skill = request.GET.get('skill')
	obj = EmployeeModel.objects.filter(skills__icontains = skill)
	print(obj)
	return obj

class Search(ListView):
	template_name = 'Home/AllAdvertisiments.html'
	paginate_by = 10

	def get_queryset(self):
		if self.kwargs and self.kwargs == 'category_id':
			return redirect(reverse('AdByCategory' , kwargs = {"category_id":self.kwargs == 'category_id'}))
		else:
			if self.request.GET.get('skill'):
				return search_employee(self.request)
			else:
				return search_filter(self.request)


	def get_context_data(self , **kwargs):
		context = super(Search , self).get_context_data(**kwargs)
		context['SearchForm'] = SearchForm
		context['request'] = self.request
		context['title'] = 'آگهی ها'
		return context
