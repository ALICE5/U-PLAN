from django.db import models

# Create your models here.

class Index(models.Model):
	name = models.CharField(null=True,blank=True,max_length=200)
	def __init__(self):
		return self.name
		