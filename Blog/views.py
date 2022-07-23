from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class BlogHome(TemplateView):
    def get(self , request , *args , **kwargs):
        context = {'title' : 'مقالات'}
        return render(request , "Comming-soon.html" , context)
