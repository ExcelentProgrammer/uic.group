from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size_query_param = "page_size"

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size and page_size.isdigit():
            return int(page_size)
        return super().get_page_size(request)
