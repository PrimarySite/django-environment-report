Django Environment Report
--------------------------

.. image:: https://circleci.com/gh/PrimarySite/django-environment-report.svg?style=svg
    :target: https://circleci.com/gh/PrimarySite/django-environment-report

.. image:: https://codecov.io/gh/PrimarySite/django-environment-report/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/PrimarySite/django-environment-report



Report the environment of your django installation

Sometimes you need a quick look at the internals of your django website withou having to ``ssh``
into the machine. You need to be a ``superuser`` to access this view.

OS and Python Information
==========================

Displays the django, python and database versions.

Settings
=========

Displays the django settings, confidential information is replaced by stars.

Installed Packages
===================

Display the installed python packes and their versions like ``pip freeze``.

Migrations
===========

Displays the migrations that have been applied and when they were applied.

Locales
========

Display information about the system ``Locale``.

Install
--------

``pip install djenvrep``

Add ``url(r'^/admin/settings/', include('djenvrep.urls')),`` to your ``urls.py``.

Then go to ``http://localhost:8000/admin/settings/environment-settings/`` to view your environment.
