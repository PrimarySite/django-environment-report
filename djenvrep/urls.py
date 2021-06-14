# -*- coding: utf-8 -*-
"""Django Environment Report Urls."""

# Django
from django.conf.urls import url

# Local
from .views import environment_settings_view

urlpatterns = [
    url(r"^environment-settings/$", environment_settings_view, name="environment_settings_view",),
]
