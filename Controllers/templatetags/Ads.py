from django import template
from Employer.models import Advertisement
from django.utils import timezone
from Employer.models import Manager

now = timezone.now()

register = template.Library()

@register.inclusion_tag('Employer/Advertising.html')
def home_ads():
	qs = Advertisement.objects.filter(company__valid = True, expired_in__gt = now)
	context = {
	'Ads':qs
	}
	return context
