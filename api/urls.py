from django.urls import path, include
from .views import categorylist
urlpatterns = [
   path('category/',categorylist)
]