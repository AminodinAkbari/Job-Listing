from django.urls import path
from django.contrib.auth.decorators import login_required

from Accounts.views import EmployeeRegisterView
from Employee.views import *
urlpatterns = [
	path('resume/<int:pk>' , login_required(UpdateResume.as_view()) , name = 'UpdateResume'),
	path('jobs-apply/<int:pk>' , login_required(EmployeeJobApply) , name = 'EmployeeJobApply'),
	path('apply/<int:ad>' , login_required(ApplicantView) , name = 'ApplicantView'),
	path('add_favorite/<int:ad>' , login_required(FavoriteView) , name = 'Favorite'),
	path('ads-saved/<int:pk>' , login_required(AdSaved) , name = 'AdsSaved'),
	path('ad-delete/<int:pk>' , login_required(AdUnsaved) , name = 'AdUnsaved'),
]