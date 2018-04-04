from django.contrib import admin
from .models import Keg, Fill, Batch, Beer


@admin.register(Keg)
class KegAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'litres', 'created')
    list_per_page = 20


@admin.register(Fill)
class FillAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'keg')
    list_per_page = 20


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'litres', 'beer', 'created')
    list_per_page = 20


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_per_page = 20
