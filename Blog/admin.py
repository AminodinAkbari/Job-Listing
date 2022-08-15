from django.contrib import admin
from Blog import models
# Register your models here.

class MainBlogModuleAdmin(admin.ModelAdmin):
	list_display = ['id' , 'short_MainBlogText' , 'category' , 'likes' , 'create_date' , 'enable']

admin.site.register(models.MainBlogModule , MainBlogModuleAdmin)
admin.site.register(models.BlogCategories)