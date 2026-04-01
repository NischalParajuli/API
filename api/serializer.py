from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        #exclude = ['id']  to exclude id field from the serialized output

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category') # to accept category id in the request data
    category = serializers.StringRelatedField() # to display category name instead of id
    price_with_vat = serializers.SerializerMethodField() # to calculate price with VAT
    price_with_discount = serializers.SerializerMethodField() # to calculate price with discount
    class Meta:
        model = Food
        fields = '__all__'

    def get_price_with_vat(self, food):
        return food.price + food.price * 0.12  #  12% VAT
    
    def get_price_with_discount(self, food):
        return food.price - food.price * 0.1  #  10% discount


# class CategorySerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only = True)
#   name = serializers.CharField()

#   def create(self,validated_data):
#     category = Category.objects.create(name = validated_data.get('name'))
#     return category
  
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.save()
#     return instance


# class TableSerializer(serializers.Serializer): # Serializer for Table model
#     id = serializers.IntegerField(read_only=True)
#     number = serializers.CharField()
#     is_available = serializers.BooleanField()
  
#     def create(self, validated_data): # Create new instance
#         table = Table.objects.create(
#           number=validated_data.get('number'),
#           is_available=validated_data.get('is_available', False)
#         )
#         return table
    
#     def update(self, instance, validated_data): # Update existing instance
#         instance.number = validated_data.get('number', instance.number) # instance.number will be updated only if 'number' is provided in validated_data, otherwise it remains unchanged
#         instance.is_available = validated_data.get('is_available', instance.is_available)
#         instance.save()
#         return instance