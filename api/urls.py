from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category', CategoryModelViewSet, basename='category')
# router.register('category_detail', CategoryDetail, basename='category_detail')
# router.register('table', TableViewSet, basename='table')
# router.register('table_detail', TableDetail, basename='table_detail')


urlpatterns = [
    # path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<int:id>/', CategoryDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # # path('table/', TableList.as_view()),
    # # path('table/<int:id>/', TableDetail.as_view()),
] + router.urls