from django.urls import path
from Rest_API import views

urlpatterns = [
	path('test_all_ads' , views.All_Advertisements.as_view()),
	path('all_ads' , views.All_Advertisements.as_view() , name = 'All_Advertisements'),
	path('Ads-full-manage/<int:pk>' , views.Ads_FullMangement.as_view() , name = 'Ads_FullMangement'),

]