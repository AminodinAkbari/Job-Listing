from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars
import os
# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_logo_path(instance , filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title[:15]}-BlogBanner{ext}"
    return f"Blog/Banners/{final_name}"

class BlogCategories(models.Model):
	category = models.CharField(max_length = 150)
	icon = models.CharField(max_length = 150)

	def __str__(self):
		return self.category

class MainBlogModule(models.Model):
	title = models.CharField(max_length = 350 , verbose_name = 'عنوان')
	banner = models.ImageField(upload_to = upload_logo_path)
	MainBlogText = models.TextField(verbose_name = 'متن مقاله')
	category = models.ForeignKey(BlogCategories , on_delete = models.PROTECT , verbose_name = 'دسته بندی')
	likes = models.IntegerField(verbose_name = 'تعداد پسندیده ها',default=0)
	create_date = models.DateTimeField(auto_now_add = True , verbose_name = 'تاریخ ایجاد')
	enable = models.BooleanField(default = False , verbose_name = 'فعال')

	@property
	def short_MainBlogText(self):
		return truncatechars(self.MainBlogText , 50)