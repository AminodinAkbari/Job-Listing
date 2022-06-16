from django.contrib import admin
from .models import Footer , SocialLinks
# Register your models here.

class SocialAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Footer)
admin.site.register(SocialLinks , SocialAdmin)
