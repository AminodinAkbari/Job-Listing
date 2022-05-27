from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from Home.views import (
Index ,
AllAds_CBV ,
AdDetail,
AdByCategory ,
TopCompanies,
ALLEmployees,
EmployeeDetail,
ALLCompanies,
)
=======
from Home.views import Index , AllAds_CBV , AdDetail,AdByCategory , TopCompanies,ALLEmployees,EmployeeDetail
>>>>>>> f1eee86f862167e6899b4c13b52add5a0b0166fa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index , name = 'Home'),
    path('all-ads', AllAds_CBV.as_view() , name = 'AllAds'),
    path('all-employees', ALLEmployees.as_view() , name = 'AllEmployees'),
<<<<<<< HEAD
    path('all-companies', ALLCompanies.as_view() , name = 'ALLCompanies'),
=======
>>>>>>> f1eee86f862167e6899b4c13b52add5a0b0166fa
    path('ad-detail/<int:pk>', AdDetail.as_view() , name = 'AdDetail'),
    path('employer-detail/<int:pk>', EmployeeDetail.as_view() , name = 'EmployerDetail'),
    path('all-ads/<int:category_id>', AdByCategory.as_view() , name = 'AdByCategory'),
    path('Top-Companies', TopCompanies.as_view() , name = 'TopCompanies'),
]