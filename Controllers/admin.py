from django.contrib import admin
from .models import categories,Languages
# Register your models here.
admin.site.register(categories)

class LanguagesStr(admin.ModelAdmin):
	list_display = ['lang_fa_type' , 'lang_en_type']
admin.site.register(Languages,LanguagesStr)