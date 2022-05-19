from django.db import models

# Create your models here.

class Newsletter(models.Model):
	email = models.EmailField(max_length = 150)
	def __str__(self):
		return self.email