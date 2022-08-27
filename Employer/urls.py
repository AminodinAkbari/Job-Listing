from django.urls import path
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Employer import views

# from .views import 	EditMangerInfo , UpdatePasswordManager
urlpatterns = [
	path('new_ad' , login_required(views.NewAd.as_view()) , name = 'NewAd'),
	path('new_company' , login_required(views.NewCompany.as_view()) , name = 'NewCompany'),
	path('edit_manager_info/<int:pk>' , login_required(views.EditMangerInfo.as_view()) , name = 'EditManagerInfo'),
	path('edit_company_info/<int:pk>' , login_required(views.EditCompanyView.as_view()) , name = 'EditCompanyView'),
	path('update_manager_password' , login_required(views.UpdatePasswordManager.as_view()) , name = 'UpdatePasswordManager'),
	# path('updatepassword' , login_required(ChangePassword.as_view()) , name = 'ChangePassword'),
	path('manager_panel/<int:pk>' , login_required(views.ManagerPanel.as_view()) , name = 'ManagerPanel'),
	path('Message/<int:pk>' , login_required(views.MessageDetail.as_view()) , name = 'MessageDetail'),
	path('ad-applicants/<int:pk>' , login_required(views.ADApplicants.as_view()) , name = 'AdvertisementApplicants'),
	path('editad_view/<int:pk>' , login_required(views.EditAdView.as_view()) , name = 'EditAdView'),
	path('delete_ad/<int:pk>' , login_required(views.DeleteAd) , name = 'DeleteAd'),
	path('delete_company/<int:pk>' , login_required(views.DeleteCompany) , name = 'DeleteCompany'),
	path('determine_the_status/<int:pk>/<int:adver_id>' , login_required(views.determine_the_status) , name = 'DetermineTheStatus'),
	path('new_hire/<int:employee_id>' , login_required(views.NewHire.as_view()) , name = 'NewHire'),
]
