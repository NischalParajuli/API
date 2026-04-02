from django_filters import filterset
from .models import Food

class FoodFilter(filterset.FilterSet):
    class Meta:
        model = Food
        fields = {
            'name': ['icontains'],
            'price': ['gt', 'lt'],
        }