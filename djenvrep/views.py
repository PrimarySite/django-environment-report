# -*- coding: utf-8 -*-
"""Django Environment Report."""
# Future
from __future__ import absolute_import
from __future__ import unicode_literals

# Django
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views.debug import get_safe_settings

# Local
from .utils import get_db_info
from .utils import get_installed_packages
from .utils import get_migrations
from .utils import get_python_paths
from .utils import get_versions


@user_passes_test(lambda u: u.is_superuser)
def environment_settings_view(request, template_name='environment-report.html'):
    """
    Generate a report of the django environment.

    Only Superusers have access to it.
    """
    context = {
        'settings': get_safe_settings(),
        'installed_packages': get_installed_packages(),
        'versions': get_versions(),
        'python_paths': get_python_paths(),
        'db': get_db_info(),
        'migrations': get_migrations(),
    }

    return render(request, template_name, context)
