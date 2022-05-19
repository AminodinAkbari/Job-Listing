from django.shortcuts import redirect
from django import template
from Employer.models import Advertisement
from django.utils import timezone
from Employer.models import Manager
from Employer.models import Applicant
from Employee.models import Favorite

now = timezone.now()

register = template.Library()

@register.inclusion_tag('Employer/Advertising.html')
def home_ads(request):
	context = {}
	qs = Advertisement.objects.filter(company__valid = True, expired_in__gt = now).order_by('-generate_in')[:12]
	if request.user.is_authenticated:
		applied_jobs = Applicant.objects.filter(user = request.user)
		marked = Favorite.objects.filter(user = request.user)
		str_list_for_template = []
		for ad in applied_jobs:
			str_list_for_template.append(ad.ad)
		context['applied_jobs'] = str_list_for_template
		context['marked'] = marked
	context['Ads']=qs
	return context

@register.inclusion_tag('Employer/Advertising.html')
def ads_job_apply(request):
	context = {}
	context['Applicants'] = Applicant.objects.filter(user = request.user)
	context['request'] = request
	return context