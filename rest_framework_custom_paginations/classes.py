from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

"""
Custom class for django-rest-framework >= 3.1
"""


class SporePagination(PageNumberPagination):

    def custom_get_next_params(self):
        if not self.page.has_next():
            return None
        page = self.page.next_page_number()
        params = { k:(v if len(v)>1 else v[0]) for k,v in self.request.query_params.lists()}
        params['page'] = page
        return params

    def custom_get_previous_params(self):
        if not self.page.has_previous():
            return None
        page = self.page.previous_page_number()
        params = { k:(v if len(v)>1 else v[0]) for k,v in self.request.query_params.lists()}
        params['page'] = page
        return params

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('next_params', self.custom_get_next_params()),
            ('previous_params', self.custom_get_previous_params()),
            ('num_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))
