from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$',
        views.Fills.as_view({'get': 'list'}),
        name='get_fills'),
]
