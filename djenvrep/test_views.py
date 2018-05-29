# -*- coding: utf-8 -*-
"""Django Environment Report Utilities."""

# Future
from __future__ import absolute_import
from __future__ import unicode_literals

# Django
from django.contrib.auth.models import User
from django.test import RequestFactory
from django.test import TestCase

# Local
from .views import environment_settings_view


class EnvironmentSettingsViewTest(TestCase):
    """test the environment settings view."""

    def test_environment_settings_view(self):
        """Call the view to ensure it runs fine."""
        request = RequestFactory().get('/environment-settings/')
        request.user = User.objects.create_superuser('admin', 'adm@ex.test', 'T0p$3cret')
        environment_settings_view(request)
