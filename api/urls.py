from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import renderers

from .views import *

recording_list = RecordingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

recording_detail = RecordingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^$', recording_list, name='recording_list'),
    url(r'^(?P<pk>[0-9]+)/?$', recording_detail, name='recording_detail'),
]
