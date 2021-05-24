''' 自定义分页类'''
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


class DrfPaginate(PageNumberPagination):
    page_size = 10

    page_query_param = 'page'

    max_page_size = 20

    page_size_query_param = 'size'

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return page_number

    def get_paginated_response(self, data):
        return OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('content', data)
        ])
