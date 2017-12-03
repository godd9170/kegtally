from django.contrib import admin
from django.core import urlresolvers
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('qbid', 'name')
    list_per_page = 20
