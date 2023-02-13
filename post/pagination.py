from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response({
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "all_posts_count": self.page.paginator.count,
            "page_posts_count": len(self.page.object_list),
            "page_number": self.page.number,
            "all_pages_count": self.page.paginator.num_pages,
            "results": data
        })