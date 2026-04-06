from rest_framework.pagination import PageNumberPagination

class FoodPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'

class CategoryPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'

class TablePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
