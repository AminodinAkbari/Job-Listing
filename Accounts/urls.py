from django.urls import path, include
from .views import (
RegisterView,
EmployeeRegisterView,
LoginView,
LogoutView,
)
urlpatterns = [
		path('register' , RegisterView.as_view() , name = 'Register'),
		path('employee-register' , EmployeeRegisterView.as_view() , name = 'EmployeeRegister'),
		path('login' , LoginView.as_view() , name = 'Login'),
		path('logout' , LogoutView , name = 'Logout'),
]
