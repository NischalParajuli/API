from django.urls import path
from .views import *

urlpatterns = [
    path('category/', categorylist),
    path('category/<int:id>/', categoryDetail),

    path('table/', table_list),
    path('table/<int:id>/', table_detail),
]