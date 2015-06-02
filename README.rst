django-rest-custom-paginations
==============================

Custom paginations for django rest framework

Compatibility
-------------

work with :
 * Python 2.7 / 3.4
 * Dango 1.6 / 1.7
 * Django Rest Framework 2.4 / 3.0

Installation
------------

Install the package from pypi: ::

    pip install djangorestframework-custom-paginations

Add the application in your django settings: ::

    DJANGO_APPS = ('rest_framework_custom_paginations',)

Configure your rest framework : ::

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'rest_framework_custom_paginations.paginations.SporePaginationSerializer'
    }
