from django.contrib import admin
from .models import Patient
# Register your models here.

class padmin(admin.ModelAdmin):
    list_display = ['name','age','date']

admin.site.register(Patient,padmin)