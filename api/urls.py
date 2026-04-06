from django.urls import path
from .views import *
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


router = routers.SimpleRouter()
router.register('category', CategoryModelViewSet, basename='category')
router.register('table', TableModelViewSet, basename='table')
router.register('food', FoodModelViewSet, basename='food')


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + router.urls