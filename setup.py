import os
import sys

from setuptools import find_packages
from setuptools import setup

version = '0.4'

setup(name='djenvrep',
      version=version,
      description="Report the environment of your django installation.",
      long_description=(open("README.md").read() + "\n"),
      classifiers=[
          'Framework :: Django',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.11',
          'Framework :: Django :: 2.0',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          #'Development Status :: 5 - Production/Stable',
      ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='https://github.com/PrimarySite/django-environment-report',
      license='MIT',
      packages=find_packages(exclude=['tests', 'testproj']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'Django',
      ],
      entry_points="""
        # -*- Entry points: -*-
        """,
      )
