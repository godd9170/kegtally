import os
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inventory/', include('inventory.urls'))
]
