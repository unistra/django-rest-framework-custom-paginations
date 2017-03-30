django-rest-framework-custom-paginations
========================================

Custom paginations for django rest framework

Compatibility
-------------

work with :
 * Python 2.7 / 3.4
 * Dango 1.6 / 1.7
 * Django Rest Framework 2.4 / 3.0 / 3.1 / 3.2 / 3.3

Installation
------------

Install the package from pypi: ::

    pip install djangorestframework-custom-paginations

Add the application in your django settings: ::

    DJANGO_APPS = ('rest_framework_custom_paginations',)

Configure your rest framework for DRF >= 3.1: ::

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework_custom_paginations.class.SporePagination',
    }

or configure your rest framework for DRF < 3.1: ::

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'rest_framework_custom_paginations.paginations.SporePaginationSerializer'
    }

Usage
-----

Add the following parameters in a ListAPIView : ::

    class PersonList(generics.ListAPIView):
        """ list of person """
        ...
        paginate_by = 100
        paginate_by_param = 'page_size'
        max_paginate_by = 500

Example
-------

Results of Spore Pagination : ::

    {
        "count": 532,
        "next": "http://myurls/persons.json?structure=mystructure&page=3",
        "next_params": {
            "page": 3,
            "structure": "mystructure"
        },
        "num_pages": 6,
        "previous": "http://myurls/persons.json?structure=mystructure&page=1",
        "previous_params": {
            "page": 1,
            "structure": "mystructure"
        },
        "results": [
            ...
        ]
    }
