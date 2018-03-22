from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$',
        views.Fills.as_view({'get': 'list'}),
        name='get_fills'),
    url(r'^batches/',
        views.Batches.as_view({'get': 'list'}),
        name='get_batches'),
    url(r'^(?P<uuid>[^/]+)/$',
        views.FillBill.as_view(),
        name='fill'),
    url(r'^kegs/(?P<uuid>[^/]+)/$',
        views.KegDetail.as_view(),
        name='fill'),
]
