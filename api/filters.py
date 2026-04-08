from django_filters import FilterSet
from .models import Food

class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'name': ['icontains'],
            'price': ['gt', 'lt'],
        }