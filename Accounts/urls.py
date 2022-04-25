from django.urls import path, include
from .views import (
RegisterView,
LoginView,
LogoutView,
)
urlpatterns = [
path('register' , RegisterView.as_view() , name = 'Register'),
path('login' , LoginView , name = 'Login'),
path('logout' , LogoutView , name = 'Logout'),
]