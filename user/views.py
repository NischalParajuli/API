from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class LoginView(APIView):
    """Authenticate users and return an auth token."""

    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')

        if phone == '' or password == '':
            return Response({"detail": "Phone and password are required."}, status=400)

        user = authenticate(phone=phone, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "username": f"Login successful for user: {phone}",
                "token": token.key,
            })

        return Response({"detail": "Invalid credentials."}, status=401)
