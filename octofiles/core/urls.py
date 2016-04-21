# -*- coding: utf-8 -*-

from django.conf.urls import url
from octofiles.core.views import DocumentView


urlpatterns = [
    url(r'$', DocumentView.as_view(), name='list'),
]
