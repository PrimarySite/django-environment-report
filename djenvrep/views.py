# -*- coding: utf-8 -*-
"""Django Environment Report."""

# Django
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Local
from .utils import get_db_info
from .utils import get_installed_packages
from .utils import get_locale_info
from .utils import get_migrations
from .utils import get_python_paths
from .utils import get_system_locales
from .utils import get_versions

try:
    from django.views.debug import SafeExceptionReporterFilter
    get_safe_settings = SafeExceptionReporterFilter().get_safe_settings()
except AttributeError:
    from django.views.debug import get_safe_settings


@user_passes_test(lambda u: u.is_superuser)
def environment_settings_view(request, template_name="environment-report.html"):
    """
    Generate a report of the django environment.

    Only Superusers have access to it.
    """
    context = {
        "settings": get_safe_settings(),
        "installed_packages": get_installed_packages(),
        "versions": get_versions(),
        "python_paths": get_python_paths(),
        "db": get_db_info(),
        "migrations": get_migrations(),
        "locales": get_system_locales(),
        "locale_info": get_locale_info(),
    }

    return render(request, template_name, context)
