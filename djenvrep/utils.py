# -*- coding: utf-8 -*-
"""Django Environment Report Utilities."""

# Future
from __future__ import absolute_import
from __future__ import unicode_literals

# Standard Library
import locale
import os
import platform
import sys

# Django
import django
from django.db import connection
from django.db.migrations.recorder import MigrationRecorder

try:  # pragma: nocover
    from pip._internal.operations import freeze
except ImportError:  # pragma: nocover
    from pip.operations import freeze


def get_installed_packages():
    """Get all installed packages with `pip freeze`."""
    packages = list(freeze.freeze())
    packages.sort()
    installed = dict()
    for package in packages:
        try:
            name, version = package.split('==')
        except ValueError:
            name = package
            version = 'Unknown'
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


def get_migrations():
    """Get the migrations."""
    return MigrationRecorder.Migration.objects.all()


def get_system_locales():
    """Get system locale settings."""
    locales = dict()
    for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
        locales[env_name] = os.environ.get(env_name, 'Not Set')

    locales['Default locale'] = locale.getdefaultlocale()
    locales['Locale from environment'] = locale.getlocale()
    locales['Preferred encoding'] = locale.getpreferredencoding()
    return locales


def get_locale_info():
    """Get the details of the locale."""
    sign_positions = {
        0: 'Surrounded by parentheses',
        1: 'Before value and symbol',
        2: 'After value and symbol',
        3: 'Before value',
        4: 'After value',
        locale.CHAR_MAX: 'Unspecified',
    }
    info = dict()
    info.update(locale.localeconv())
    info['p_sign_posn'] = sign_positions[info['p_sign_posn']]
    info['n_sign_posn'] = sign_positions[info['n_sign_posn']]
    # convert the currency symbol to unicode
    try:
        info['currency_symbol_u'] = info['currency_symbol'].decode('utf-8')
    except AttributeError:
        info['currency_symbol_u'] = info['currency_symbol']
    return info
