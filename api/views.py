# from typing import Generic
# from urllib import request
from django.shortcuts import render
# import rest_framework
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
# from rest_framework.views import APIView
from rest_framework import mixins
# from rest_framework.generics import GenericAPIView
# from rest_framework import generics

from rest_framework.viewsets import ModelViewSet, ViewSet
from .pagination import FoodPagination , CategoryPagination , TablePagination
# -------------------------------ModelViewSet-----------------------------------------------

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def destroy (self, request, id):
        category = Category.objects.get(id=id)
        items = OrderItem.objects.filter(food__category=category).count()
        if items > 0:
            return Response({"detail": "protected error: Data cannot be deleted"})
        category.delete()
        return Response({"detail": "Data has been deleted."})


class TableModelViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    pagination_class = TablePagination

    def destroy (self, request, id):
        table = Table.objects.get(id=id)
        items = OrderItem.objects.filter(table=table).count()
        if items > 0:
            return Response({"detail": "protected error: Data cannot be deleted"})
        table.delete()
        return Response({"detail": "Data has been deleted."})


from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FoodFilter
class FoodModelViewSet(ModelViewSet):
    queryset = Food.objects.all().select_related('category')
    serializer_class = FoodSerializer
    pagination_class = FoodPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    # filterset_fields = ['category']
    filterset_class = FoodFilter




#-------------------------------Function-Based Views-----------------------------------------------

# @api_view(['GET', 'POST'])
# def categorylist(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":   # FIXED
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['GET', 'PUT','DELETE'])
# def categoryDetail(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response({"detail": "Not found"}, status=404)

#     if request.method == "GET":
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     elif request.method == "PUT": # Update all fields
#         serializer = CategorySerializer(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     elif request.method == "DELETE":
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         category.delete()
#         return Response({"detail": "Data has been deleted."})
    

#     # crud operations for tablelist and tabledetails 

# @api_view(['GET', 'POST'])
# def table_list(request):
#         if request.method == "GET":
#             table = Table.objects.all()
#             serializer = TableSerializer(table, many=True)
#             return Response(serializer.data)
        
#         elif request.method == "POST":
#             serializer = TableSerializer(data = request.data)
#             serializer.is_valid(raise_exception = True)
#             serializer.save()
#             return Response(serializer.data)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def table_detail(request, id):
#         try:
#             table = Table.objects.get(id = id)
#         except Table.DoesNotExist:
#             return Response({"detail": "Not found"}, status = 404)
        
#         if request.method == "GET":
#             serializer = TableSerializer(table)
#             return Response(serializer.data)
        
#         elif request.method =="PUT": # Update all fields
#             serializer = TableSerializer(table,data = request.data)
#             serializer.is_valid(raise_exception = True)
#             serializer.save()
#             return Response(serializer.data)
        
#         elif request.method == "DELETE":
#             serializer = TableSerializer(table)
#             serializer.is_valid(raise_exception = True)
#             serializer.save()
#             return Response({"detail": "Data has been deleted."})


# ------------------------------Class-Based Views-----------------------------------------------
        
# class CategoryList(APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data , status=201)
    
# class CategoryDetail(APIView):
#     def get(self,request, id):
#         category = Category.objects.get(id=id)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
        
#     def put(self, request, id):
#         category = Category.objects.get(id=id)
#         serializer = CategorySerializer(category, data=request.data , partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def patch(self, request, id):
#         category = Category.objects.get(id=id)
#         serializer = CategorySerializer(category, data=request.data , partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         category = Category.objects.get(id=id)
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         category.delete()
#         return Response({"detail": "Data has been deleted."})
    
# class TableList(APIView):
#     def get(self, request):
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = TableSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data , status=201)
    
# class TableDetail(APIView):
#     def get(self,request,id):
#         table = Table.objects.get(id = id)
#         serializer = TableSerializer(table)
#         return Response(serializer.data)
    
#     def put(self,request, id):
#         table = Table.objects.get(id=id)
#         serializer = TableSerializer(table,data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def patch(self,request,id):
#         table = Table.objects.get(id=id)
#         serializer = TableSerializer(table,data = request.data , partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         table = Table.objects.get(id=id)
#         table.delete()
#         return Response({"detail": "Data has been deleted."})

#-----------------------------------Generic Class-Based Views-----------------------------------------------

# class CategoryGeneric(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)

# class CategoryDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'id'

#     def get(self, request, id):
#         return self.retrieve(request, id=id)
    
#     def put(self, request, id):
#         return self.update(request, id=id)
    
#     def patch(self, request, id):
#         return self.update(request, id=id)
    
#     def delete(self, request, id):
#         category = self.get_object()
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         return self.destroy(request, id=id)
    
# class TableGenerics(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer



#     def get(self,request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class TableDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
#     lookup_field = 'id'

#     def get(self,request,id):
#         return self.retrieve(request , id = id)
    
#     def put(self, request, id):
#         return self.update(request, id=id)
    
#     def patch(self, request, id):
#         return self.update(request, id=id)
    
#     def delete(self, request, id):
#         category = self.get_object()
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         return self.destroy(request, id=id)

# -----------------------------------Generic Class-Based Views with Mixins-----------------------------------------------
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'id'

#     def delete(self, request, id):
#         category = self.get_object()
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         return self.destroy(request, id=id)
    

# class TableList(generics.ListCreateAPIView):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer

# class TableDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer
#     lookup_field = 'id'

#     def delete(self, request, id):
#         table = self.get_object()
#         items = OrderItem.objects.filter(table=table).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         return self.destroy(request, id=id)


#-----------------------------------ViewSets-----------------------------------------------
# class CategoryViewSet(ViewSet):
#   def list(self, request):
#     category = Category.objects.all()
#     serializer = CategorySerializer(category, many=True)
#     return Response(serializer.data)
  
#   def create(self, request):
#     serializer = CategorySerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data , status=201)
  
# class CategoryDetail(ViewSet):
#     def retrieve(self, request, id):
#         category = Category.objects.get(id=id)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    
#     def update(self, request, id):
#         category = Category.objects.get(id=id)
#         serializer = CategorySerializer(category, data=request.data , partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


#     def destroy(self, request, id):
#         category = Category.objects.get(id=id)
#         items = OrderItem.objects.filter(food__category=category).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         category.delete()
#         return Response({"detail": "Data has been deleted."})
    
# class TableViewSet(ViewSet):
#     def list(self, request):
#         table = Table.objects.all()
#         serializer = TableSerializer(table, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = TableSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data , status=201)  

# class TableDetail(ViewSet):

#     def retrieve(self, request, id):
#         table = Table.objects.get(id=id)
#         serializer = TableSerializer(table)
#         return Response(serializer.data)

#     def update(self, request, id):
#         table = Table.objects.get(id=id)
#         serializer = TableSerializer(table, data=request.data , partial = True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def destroy(self, request, id):
#         table = Table.objects.get(id=id)
#         items = OrderItem.objects.filter(table=table).count()
#         if items > 0:
#             return Response({"detail": "protected error: Data cannot be deleted"})
#         table.delete()
#         return Response({"detail": "Data has been deleted."})
    

    

    