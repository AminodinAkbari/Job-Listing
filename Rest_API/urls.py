from django.urls import path
from Rest_API import Employer_API , Employee_API

urlpatterns = [
	#--------------Manager--------------
	path('Ads-managers-APIView' , Employer_API.AllManagers.as_view() , name = 'AllManagers'),
	path('Ads-managers-APIView/<int:pk>' , Employer_API.RetriveManager.as_view() , name = 'Manager_detail'),
	path('Ads-managers-CBV' , Employer_API.AllManagers_GEN.as_view() , name = 'AllManagers_CBV'),
	path('Ads-managers-CBV/<int:pk>' , Employer_API.RetriveManager_GEN.as_view() , name = 'RetriveManager_GENERIC'),
	path('Ads-managers-FBV' , Employer_API.all_managers_FBV_list , name = 'AllManagers_FBV_list'),
	path('Ads-managers-FBV/<int:pk>' , Employer_API.all_managers_FBV_detail , name = 'AllManagers_FBV_detail'),
	path('manager/<int:pk>' , Employer_API.EmployerDetail.as_view() , name = 'EmployerDetail'),
	#--------------Company--------------
	path('companies/' , Employer_API.AllCompanies.as_view() , name = 'AllCompanies'),
	path('companies/<int:pk>' , Employer_API.CompaniesDetail.as_view() , name = 'AllCompanies'),
	#--------------Advertisement--------------
	path('all-ads' , Employer_API.ALLAds.as_view() , name = 'ALLAds'),
	path('ad_detail/<int:pk>' , Employer_API.ADDetail.as_view() , name = 'ADDetail'),
	#------------- Applicant -------------------
	path('all-applicants/' , Employer_API.AllApplicants.as_view() , name = 'AllApplicants'),
	path('all-applicants/<int:pk>' , Employer_API.ApplicantDetail.as_view() , name = 'ApplicantDetailAPI'),
	# ----------- Hire -----------------
	path('all-hires/' , Employer_API.AllHires.as_view() , name = 'AllHires'),
	path('all-hires/<int:pk>' , Employer_API.HireDetail.as_view() , name = 'HireDetail'),

	#----------- Employees -------------
	path('all-employees/<pk>' , Employee_API.AllEmployees.as_view({'get' : 'retrive'}) , name = 'AllEmployees_Retrive'),
	path('all-employees' , Employee_API.AllEmployees.as_view({'get':'list'}) , name = 'AllEmployees_List'),
	path('new_employee' , Employee_API.RegisterNewEmployee.as_view() , name = 'NewEmployee'),
	path('edit_employee/<int:pk>' , Employee_API.EditEmployee.as_view() , name = 'EditEmployee'),
	path('employee_favorites' , Employee_API.FavoriteListOnly.as_view() , name = 'FavoriteListOnly'),
	path('employee_favorite/<int:pk>' , Employee_API.FavoriteDetail.as_view() , name = 'FavoriteRetrieve'),
]
