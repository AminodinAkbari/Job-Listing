from django.shortcuts import redirect, render , reverse , get_object_or_404
from Employer.models import Manager , Advertisement , Applicant
from Employee.models import EmployeeModel

from django.core.exceptions import ValidationError
from django.views.generic import ListView

from .forms import SearchForm

from django.utils import timezone
now = timezone.now()

# Create your views here.

def employee_owner_can_access(func):
	def wrapper(request ,pk , *args , **kwargs):
		employee = get_object_or_404(EmployeeModel,employee = pk)
		if employee.employee != request.user:
			return redirect('/')
		return func(request , pk ,*args , **kwargs , employee = employee)
	return wrapper

def file_size(value):
	limit = 2 * 1024 * 1024
	if value.size > limit:
		raise ValidationError('حجم تصویر زیاد است ! اندازه فایل نباید بالای 2مگابایت باشد')

def is_valid_queryparam(param):
    return param != '' and param is not None and param != '0'

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
	obj = EmployeeModel.objects.all()
	skill = request.GET.get('skill')
	location = request.GET.get('location')
	soldier_service = request.GET.get('soldier_service')
	if is_valid_queryparam(skill):
		obj = obj.filter(skills__icontains = skill)
	if is_valid_queryparam(location):
		obj = obj.filter(state__iexact = location)
	if is_valid_queryparam(soldier_service):
		obj = obj.filter(soldier_ship__icontains = soldier_service)
	if is_valid_queryparam(location) and is_valid_queryparam(skill):
		obj = obj.filter(state__iexact = location , skills__icontains = skill)
	return obj

class Search(ListView):
	template_name = 'Home/AllAdvertisiments.html'
	paginate_by = 10
	def get_queryset(self):
		if self.kwargs and self.kwargs == 'category_id':
			return redirect(reverse('AdByCategory' , kwargs = {"category_id":self.kwargs == 'category_id'}))
		else:
			if self.request.session['TYPE'] == 'Employer':
				return search_employee(self.request)
			else:
				return search_filter(self.request)
	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['SearchForm'] = SearchForm
		context['title'] = 'آگهی ها'
		return context


#handeling error pages
def error_404_view(request, exception):
	return render(request , 'Home/404.html' , {'title' : 'صفحه مورد نظر یافت نشد'})
