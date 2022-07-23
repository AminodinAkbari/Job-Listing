from django.urls import path
from Blog.views import BlogHome
urlpatterns = [
    path('Blog' , BlogHome.as_view() , name = 'BlogHomePage')
]
