from rest_framework.pagination import PageNumberPagination


class SnackPagination(PageNumberPagination):
    page_size = 10