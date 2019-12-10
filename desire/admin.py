from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Desire)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'avatar', 'desire')
