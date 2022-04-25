from django.urls import path
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .views import (
	NewAd,
	NewCompany,
)
urlpatterns = [
	path('new_ad' , login_required(NewAd) , name = 'NewAd'),
	path('new_company' , login_required(NewCompany) , name = 'NewCompany'),
]