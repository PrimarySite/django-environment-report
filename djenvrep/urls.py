# -*- coding: utf-8 -*-
"""Django Environment Report Urls."""

# Django
from django.conf.urls import re_path

# Local
from .views import environment_settings_view

urlpatterns = [
    re_path(r"^environment-settings/$", environment_settings_view, name="environment_settings_view",),
]
