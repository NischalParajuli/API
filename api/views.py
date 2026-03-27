from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import CategorySerializer


@api_view(['GET' ,'POST'])
def categorylist(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category,many = True) # converts to    json 
        return Response(serializer.data)
    elif request == "POST":
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET','DELETE'])
def categoryDetail(request,id):
    category = Category.objects.get(id = id)
    if request.method == "GET":
        serializer = CategorySerializer(category) 
        return Response(serializer.data)
    elif request.method == "DELETE":
        items = OrderItem.objects.filter(food__category = category).count()
        if items > 0 :
            return Response({"detail":"protected error : Data cannot be deleted"})
        category.delete()
        return Response({"detail": "Data has been deleted."})