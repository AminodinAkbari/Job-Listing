from django.urls import path
from .views import test_seassion
urlpatterns = [
path('test_seassion',test_seassion)
]