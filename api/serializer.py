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
    
class OrderItemSerializer(serializers.ModelSerializer):
    food = serializers.StringRelatedField(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all())
    class Meta:
        model = OrderItem
        fields = ['food_id','food','quantity']
    


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_items = OrderItemSerializer(many=True)
    status = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id','user','table','status','total_price','order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        total = 0
        for item_data in order_items_data:
            food = item_data['food_id']
            quantity = item_data.get('quantity', 1)
            OrderItem.objects.create(order=order, food=food, quantity=quantity)
            total += food.price * quantity
        order.total_price = total
        order.save()
        return order
