from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import MainBlogModule

# Create your views here.
class BlogHome(TemplateView):
    def get(self , request , *args , **kwargs):
        context = {'title' : 'مقالات'}
        context['blogs'] = MainBlogModule.objects.filter(enable = True)
        return render(request , "Blog/all-blogs.html" , context)
