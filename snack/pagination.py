from rest_framework.pagination import PageNumberPagination


class SnackRequestPagination(PageNumberPagination):
    page_size = 10