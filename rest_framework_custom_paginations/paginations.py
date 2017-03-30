from rest_framework import __version__ as drf_version
from rest_framework.pagination import PaginationSerializer
import copy
if drf_version < '3.0':
    from rest_framework.serializers import Field as ReadOnlyField
else:
    from rest_framework.serializers import ReadOnlyField

"""
Custom serializer for django-rest-framework < 3.1
"""


class SporeNextPageField(ReadOnlyField):
    """
    Field that returns a link to the next page in paginated results.
    """
    page_field = 'page'

    def to_representation(self, value):
        if not value.has_next():
            return None
        page = value.next_page_number()
        request = self.context.get('request')
        params = { k:(v if len(v)>1 else v[0]) for k,v in request.QUERY_PARAMS.lists()}
        params['page'] = page
        return params

    def to_native(self, value):
        """
        DRF 2 compatibility
        """
        return self.to_representation(value)

class SporePreviousPageField(ReadOnlyField):
    """
    Field that returns a link to the previous page in paginated results.
    """
    page_field = 'page'

    def to_representation(self, value):
        if not value.has_previous():
            return None
        page = value.previous_page_number()
        request = self.context.get('request')
        params = { k:(v if len(v)>1 else v[0]) for k,v in request.QUERY_PARAMS.lists()}
        params['page'] = page
        return params

    def to_native(self,value):
        """
        DRF 2 compatibility
        """
        return self.to_representation(value)


class SporePaginationSerializer(PaginationSerializer):
    next_params = SporeNextPageField(source='*')
    previous_params = SporePreviousPageField(source='*')
    num_pages = ReadOnlyField(source='paginator.num_pages')
