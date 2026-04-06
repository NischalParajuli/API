from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializer import *
from .filters import FoodFilter
from .permission import IsAdminOrReadOnly
from .pagination import FoodPagination, CategoryPagination, TablePagination

# -------------------------------ModelViewSet-----------------------------------------------

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['name']

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        if OrderItem.objects.filter(food__category=category).exists():
            return Response({"detail": "protected error: Data cannot be deleted"}, status=400)
        return super().destroy(request, *args, **kwargs)


class TableModelViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    pagination_class = TablePagination
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        table = self.get_object()
        if Order.objects.filter(table=table).exists():
            return Response({"detail": "protected error: Data cannot be deleted"}, status=400)
        return super().destroy(request, *args, **kwargs)


class FoodModelViewSet(ModelViewSet):
    queryset = Food.objects.all().select_related('category')
    serializer_class = FoodSerializer
    pagination_class = FoodPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = FoodFilter


# Legacy view examples were removed from this file for clarity.
