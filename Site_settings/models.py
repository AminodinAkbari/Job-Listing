from django.db import models

# Create your models here.
class Footer(models.Model):
    logo_fa       = models.CharField(max_length = 30,verbose_name = 'لوگو')
    logo_en       = models.CharField(max_length = 30,verbose_name = 'لوگو به انگلیسی' ,blank=True , null = True)
    short_text = models.CharField(max_length = 130 , verbose_name = 'متن کوتاه')
    email      = models.EmailField(verbose_name = 'ایمیل')
    active     = models.BooleanField(default = False,verbose_name = 'فعال')

    def __str__(self):
        return self.short_text

class SocialLinks(models.Model):
    name = models.CharField(max_length = 100 , verbose_name = 'نام به لاتین (مثلا instagram)')
    link = models.URLField(max_length = 350 , verbose_name = 'لینک')
