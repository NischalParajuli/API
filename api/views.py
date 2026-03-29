from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET', 'POST'])
def categorylist(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    elif request.method == "POST":   # FIXED
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT','DELETE'])
def categoryDetail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({"detail": "Not found"}, status=404)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT": # Update all fields
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        items = OrderItem.objects.filter(food__category=category).count()
        if items > 0:
            return Response({"detail": "protected error: Data cannot be deleted"})
        category.delete()
        return Response({"detail": "Data has been deleted."})
    

    # crud operations for tablelist and tabledetails 

@api_view(['GET', 'POST'])
def table_list(request):
        if request.method == "GET":
            table = Table.objects.all()
            serializer = TableSerializer(table, many=True)
            return Response(serializer.data)
        
        elif request.method == "POST":
            serializer = TableSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET', 'PUT', 'DELETE'])
def table_detail(request, id):
        try:
            table = Table.objects.get(id = id)
        except Table.DoesNotExist:
            return Response({"detail": "Not found"}, status = 404)
        
        if request.method == "GET":
            serializer = TableSerializer(table)
            return Response(serializer.data)
        
        elif request.method =="PUT":
            serializer = TableSerializer(table,data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        
        elif request.method == "DELETE":
            serializer = TableSerializer(table)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response({"detail": "Data has been deleted."})
        