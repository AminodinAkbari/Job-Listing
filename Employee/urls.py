from django.urls import path
from django.contrib.auth.decorators import login_required

from Accounts.views import EmployeeRegisterView
from Employee.views import *
urlpatterns = [
	path('resume/<int:pk>' , login_required(UpdateResume.as_view()) , name = 'UpdateResume'),
	path('edit-name-or-email/<int:pk>' , login_required(EditNameOrEmail_Employee.as_view()) , name = 'EditNameOrEmail-Employee'),
	path('jobs-apply' , login_required(EmployeeJobApply.as_view()) , name = 'EmployeeJobApply'),
	path('apply/<int:ad>' , login_required(ApplicantView) , name = 'ApplicantView'),
	path('applicant-detail/<int:pk>' , login_required(ApplicantDetail.as_view()) , name = 'ApplicantDetail'),
	path('canceling_applicant/<int:pk>' , login_required(canceling_applicant) , name = 'CancelingApplicant'),
	path('add_favorite/<int:ad>' , login_required(AdSaved) , name = 'Favorite'),
	path('ads-saved/' , login_required(EmployeeJobMarked.as_view()) , name = 'AdsSaved'),
	path('ad-delete/<int:pk>' , login_required(AdUnsaved) , name = 'AdUnsaved'),
	path('hire-messages/<int:pk>' , login_required(HiresList.as_view()) , name = 'HiresList'),
]
