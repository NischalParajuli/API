from django.urls import path, include
from .views import *
urlpatterns = [
   path('category/',categorylist),
   path('category/<id>/',categoryDetail)
]