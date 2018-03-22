from django.contrib import admin
from .models import QuickbooksCredentials


@admin.register(QuickbooksCredentials)
class QuickbooksCredentialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'clientSecret', 'realmId',
                    'authorizationCode', 'accessToken')
    list_per_page = 20
