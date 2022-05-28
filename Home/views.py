from django.shortcuts import render
from django.views.generic import ListView , DetailView

from Controllers.views import Who_is
from Controllers.models import categories ,job_nature
from Employer.models import Manager,Advertisement,Company
from Employee.models import EmployeeModel

from datetime import datetime
from django.utils import timezone

from Accounts.models import Newsletter
from Accounts.forms import NewsletterEmailsForm
from django.conf import settings
from django.core.mail import send_mail

now = timezone.now()

@Who_is
def Index(request , user_type):
	context = {}
	Categories = categories.objects.all()
	All_emails = Newsletter.objects.all()
	companies  = Company.objects.all()
	top_companies = Company.objects.annotate(num_ad=Count('company')).order_by('-num_ad')[:5]
	context['categories'] = Categories
	context['companies'] = companies
	context['top_companies'] = top_companies
	context['employees'] = EmployeeModel.objects.all()
	context['is_a_manager'] = user_type
	if request.method == 'POST':
		form = NewsletterEmailsForm(request.POST)
		context['Newsletter'] = form
		if form.is_valid():
			user_email = form.cleaned_data.get('email')
			subject = 'خوش آمد گویی از تیم Skill Hunt'
			message = 'سلام شما در خبرنامه ما عضو شدید'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user_email,]
			send_mail( subject, message, email_from, recipient_list )
			form.save()	
	else:
		context['Newsletter'] = NewsletterEmailsForm()
	return render(request , 'index.html' , context)

# _______All Ads Filtering __________
def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
	obj = Advertisement.objects.filter(expired_in__gt = now)
	category = request.GET.get('category')
	location = request.GET.get('location')
	job_nature = request.GET.get('job_nature')
	if is_valid_queryparam(category):
		obj = obj.filter(category__name__iexact = category )
	if is_valid_queryparam(location):
		obj = obj.filter(location__icontains = location)
	if is_valid_queryparam(job_nature):
		obj = obj.filter(job_nature__iexact = job_nature)
	return obj

class AllAds_CBV(ListView):
	template_name = 'Home/AllAdvertisiments.html'
	paginate_by = 9
	def get_queryset(self):
		return filter(self.request)
	def get_context_data(self,**kwargs):
		context = super(AllAds_CBV,self).get_context_data(**kwargs)
		Categories = categories.objects.all()
		# context['page_obj'] = Advertisement.objects.filter(expired_in__gt = now)
		context['request'] = self.request
		context['title'] = 'آگهی ها'
		context['categories'] = Categories
		context['job_nature_choices'] = job_nature

		return context
# ___________End All Ads __________________
# ___________ALL EMPLOYEES and ALL EMPLOYERS_________________

class ALLEmployees(ListView):
	template_name = 'Home/All-Employees.html'
	paginate_by = 9

	def get_queryset(self):
		return EmployeeModel.objects.all()

	def get_context_data(self , **kwargs):
		context = super(ALLEmployees,self).get_context_data(**kwargs)
		context['title'] = 'لیست کارجویان'
		return context

class ALLCompanies(ListView):
	template_name = 'Home/All-Employers.html'
	paginate_by = 9

	def get_queryset(self):
		return Company.objects.all()

	def get_context_data(self , **kwargs):
		context = super(ALLCompanies,self).get_context_data(**kwargs)
		context['title'] = 'لیست شرکت ها'
		return context

# ___________END______________
class AdDetail(DetailView):
	model = Advertisement
	template_name = 'Employer/AdvertimentDetail.html'

	def get_context_data(self , **kwargs):
		context = super(AdDetail , self).get_context_data(**kwargs)
		obj = self.get_object()
		time_left = obj.expired_in.day-now.day
		Skills = []
		if self.request.user.is_authenticated:
			try:
				employee = EmployeeModel.objects.get(employee = self.request.user)
			except:
				employee = None
			if employee is not None:
				context['employee'] = employee
		context['skills'] = self.object.skills.split('/')
		context['title'] = self.object.title
		context['time_left'] = time_left
		return context

class EmployeeDetail(DetailView):
	model = EmployeeModel
	template_name = 'Employee/EmployeeDetail.html'

	def get_context_data(self , **kwargs):
		context = super(EmployeeDetail , self).get_context_data(**kwargs)
		obj = self.get_object()
		context['title'] = 'رزومه کارجو'
		if obj.skills:
			context['skills'] = self.object.skills.split('/')
		return context

class AdByCategory(ListView):
	template_name = 'Home/AllAdvertisiments.html'
	paginate_by = 9

	def get_queryset(self):
		return Advertisement.objects.filter(category_id = self.kwargs['category_id'])

from django.db.models import Count

class TopCompanies(ListView):
	template_name = 'index.html'

	def get_context_data(self,**kwargs):
		context = super(TopCompanies,self).get_context_data(**kwargs)
		
		context['top_company'] = top_companies
		return context
