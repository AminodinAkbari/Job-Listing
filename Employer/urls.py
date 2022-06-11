from django.urls import path
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .views import (
	NewAd,
	NewCompany,
	ManagerPanel,
	DeleteAd,
	EditCompanyView,
	DeleteCompany,
	EditAdView,
	determine_the_status,
	NewHire,
)
from .views import 	EditMangerInfo , UpdatePasswordManager
urlpatterns = [
	path('new_ad' , login_required(NewAd.as_view()) , name = 'NewAd'),
	path('new_company' , login_required(NewCompany.as_view()) , name = 'NewCompany'),
	path('edit_manager_info/<int:pk>' , login_required(EditMangerInfo.as_view()) , name = 'EditManagerInfo'),
	path('edit_company_info/<int:pk>' , login_required(EditCompanyView.as_view()) , name = 'EditCompanyView'),
	path('update_manager_password' , login_required(UpdatePasswordManager) , name = 'UpdatePasswordManager'),
	path('manager_panel/<int:pk>' , login_required(ManagerPanel.as_view()) , name = 'ManagerPanel'),
	path('editad_view/<int:pk>' , login_required(EditAdView.as_view()) , name = 'EditAdView'),
	path('delete_ad/<int:pk>' , login_required(DeleteAd) , name = 'DeleteAd'),
	path('delete_company/<int:pk>' , login_required(DeleteCompany) , name = 'DeleteCompany'),
	path('determine_the_status/<int:pk>/<int:adver_id>' , login_required(determine_the_status) , name = 'DetermineTheStatus'),
	path('new_hire/<int:employee_id>' , login_required(NewHire.as_view()) , name = 'NewHire'),
]
