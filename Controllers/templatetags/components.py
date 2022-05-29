from django import template
from Employer.models import Applicant
from Employee.models import Favorite
register = template.Library()

@register.inclusion_tag('Components/Advertisement-component.html')
def ad_component_tag(Ads , marked=None , applied_jobs=None , request=None , applicant=None):
    context = {
    'item' : Ads ,
    }
    if request is not None:
        if request.user.is_authenticated:
            marked_list = []
            marked = Favorite.objects.filter(user = request.user)
            for item in marked:
                marked_list.append(item.ad)

            applied_jobs = Applicant.objects.filter(user = request.user)
            str_list_for_applid = []
            for ad in applied_jobs:
                str_list_for_applid.append(ad.ad)

            context['marked']=marked_list
            context['applied_jobs']=str_list_for_applid

    context['applicant'] = applicant
    context['request'] = request
    return context
