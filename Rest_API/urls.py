from django.urls import path
from Rest_API import views , Employer_API

urlpatterns = [
	path('test_all_ads' , views.All_Advertisements.as_view()),
	path('all_ads' , views.All_Advertisements.as_view() , name = 'All_Advertisements'),
	path('Ads-full-manage/<int:pk>' , views.Ads_FullMangement.as_view() , name = 'Ads_FullMangement'),

	path('Ads-managers-APIView' , Employer_API.AllManagers.as_view() , name = 'AllManagers'),
	path('Ads-managers-APIView/<int:pk>' , Employer_API.RetriveManager.as_view() , name = 'Manager_detail'),
	path('Ads-managers-CBV' , Employer_API.AllManagers_GEN.as_view() , name = 'AllManagers_CBV'),
	path('Ads-managers-CBV/<int:pk>' , Employer_API.RetriveManager_GEN.as_view() , name = 'RetriveManager_GENERIC'),
	path('Ads-managers-FBV/' , Employer_API.all_managers_FBV_list , name = 'AllManagers_FBV_list'),
	path('Ads-managers-FBV/<int:pk>' , Employer_API.all_managers_FBV_detail , name = 'AllManagers_FBV_detail'),
	path('manager/<int:pk>' , Employer_API.EmployerDetail.as_view() , name = 'EmployerDetail'),
]
