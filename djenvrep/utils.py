# -*- coding: utf-8 -*-
"""Django Environment Report Utilities."""

# Future
from __future__ import absolute_import
from __future__ import unicode_literals

# Standard Library
import platform
import sys

# Django
import django
from django.db import connection

try:  # pragma: nocover
    from pip._internal.operations import freeze
except ImportError:  # pragma: nocover
    from pip.operations import freeze


def get_installed_packages():
    """Get all installed packages with `pip freeze`."""
    packages = list(freeze.freeze())
    installed = dict()
    for package in packages:
        name, version = package.split('==')
        installed[name] = version
    return installed


def get_versions():
    """Get version information."""
    versions = dict()
    versions['python'] = sys.version
    versions['platform'] = platform
    versions['django'] = django.get_version()
    return versions


def get_python_paths():
    """Get Python path information."""
    return sys.path


def get_db_info():
    """Get current django db connection information."""
    db_info = dict()
    db_info['vendor'] = connection.vendor
    if connection.vendor == 'postgresql':  # pragma: nocover
        db_info['version'] = connection.pg_version
    else:
        db_info['version'] = 'unknown'
    return db_info
