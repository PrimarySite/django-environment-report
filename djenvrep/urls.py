# -*- coding: utf-8 -*-
"""Django Environment Report Urls."""

# Future
from __future__ import absolute_import
from __future__ import unicode_literals

# Django
from django.conf.urls import url

# Local
from .views import environment_settings_view

urlpatterns = [
    url(r'^environment-settings/$',
        environment_settings_view,
        name='environment_settings_view',
        ),
]
