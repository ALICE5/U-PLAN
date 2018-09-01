from django.db import models

# Create your models here.

class Index(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    def __str__(self):
        return self.name

class About(models.Model):
    title = models.IntegerField(max_length=100)
    def __str__(self):
        return self.title