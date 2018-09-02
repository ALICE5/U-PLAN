from django.contrib import admin

# Register your models here.

from firstapp.models import Index
from firstapp.models import About
admin.site.register(Index)
admin.site.register(About)
