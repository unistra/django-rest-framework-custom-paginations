from rest_framework import pagination
from rest_framework import serializers
import copy


class SporeNextPageField(serializers.Field):
    """
    Field that returns a link to the next page in paginated results.
    """
    page_field = 'page'

    def to_native(self, value):
        if not value.has_next():
            return None
        page = value.next_page_number()
        request = self.context.get('request')
        params = copy.deepcopy(request.QUERY_PARAMS)
        params['page'] = page
        return params


class SporePreviousPageField(serializers.Field):
    """
    Field that returns a link to the previous page in paginated results.
    """
    page_field = 'page'

    def to_native(self, value):
        if not value.has_previous():
            return None
        page = value.previous_page_number()
        request = self.context.get('request')
        params = copy.deepcopy(request.QUERY_PARAMS)
        params['page'] = page
        return params


class SporePaginationSerializer(pagination.PaginationSerializer):
    next_params = SporeNextPageField(source='*')
    previous_params = SporePreviousPageField(source='*')
    num_pages = serializers.Field(source='paginator.num_pages')
