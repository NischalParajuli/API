from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
class LoginView(APIView):
  def post(self,request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username == ''  or password == '':
      return Response({"detail": "Username and password are required."}, status=400)
    user = authenticate(username=username, password=password)
    if user:
      token,_ = Token.objects.get_or_create(user=user)
      return Response({"username":f"Login successful for user: {username}", "token": token.key})
    return Response({"detail": "Invalid credentials."}, status=401)