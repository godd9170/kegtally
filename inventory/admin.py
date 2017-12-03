from django.contrib import admin
from django.core import urlresolvers
from .models import Keg, Fill, Batch, Beer


@admin.register(Keg)
class KegAdmin(admin.ModelAdmin):
    list_display = ('id', 'litres', 'created')
    list_per_page = 20


@admin.register(Fill)
class FillAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')
    list_per_page = 20


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'litres', 'beer', 'created')
    list_per_page = 20


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_per_page = 20
