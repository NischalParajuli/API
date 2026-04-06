from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""

    class Meta:
        model = Category
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    """Serializer for Table model."""

    class Meta:
        model = Table
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category'
    )
    category = serializers.StringRelatedField()
    price_with_vat = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = '__all__'

    def get_price_with_vat(self, food):
        """Calculate price including VAT."""
        return food.price + food.price * 0.12

    def get_price_with_discount(self, food):
        """Calculate discounted price."""
        return food.price - food.price * 0.1
