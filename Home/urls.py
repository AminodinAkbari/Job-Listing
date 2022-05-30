from django.contrib import admin
from django.urls import path, include
from Home.views import (
Index ,
AdDetail,
AdByCategory ,
TopCompanies,
ALLEmployees,
EmployeeDetail,
ALLCompanies,
CompanyView,
)
from Controllers.views import Search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index , name = 'Home'),
    path('all-employees', ALLEmployees.as_view() , name = 'AllEmployees'),
    path('all-companies', ALLCompanies.as_view() , name = 'ALLCompanies'),
    path('ad-detail/<int:pk>', AdDetail.as_view() , name = 'AdDetail'),
    path('employer-detail/<int:pk>', EmployeeDetail.as_view() , name = 'EmployerDetail'),
    path('all-ads/<int:category_id>', Search.as_view() , name = 'AdByCategory'),
    path('Top-Companies', TopCompanies.as_view() , name = 'TopCompanies'),
    path('Detail-Companies/<int:pk>', CompanyView.as_view() , name = 'CompanyView'),
]
