from django import template
from Controllers.forms import SearchForm
from Employer.models import Manager
from Employee.models import EmployeeModel
from Controllers.models import categories
from Controllers.forms import SearchForm
from Site_settings.models import Footer , SocialLinks
register = template.Library()

@register.inclusion_tag('BASE_HTMLs/Nav.html' , takes_context=True)
def Navbar(context , request):
	context['request'] = request
	context['settings'] = Footer.objects.filter(active = True).first()
	return context

@register.inclusion_tag('BASE_HTMLs/Footer.html' , takes_context=True)
def FooterComponent(context):
	footer = Footer.objects.filter(active = True).first()
	Social = SocialLinks.objects.all()
	context['Footer']  = footer
	context['Social']  = Social
	return context


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


@register.inclusion_tag('Home/Search.html')
def Search(request):
	context = {}
	context['is_a_manager'] = Manager.objects.filter(email = request.user.username).first()
	context['categories'] = categories.objects.all()
	context['SearchForm'] = SearchForm
	context['request'] = request
	return context
