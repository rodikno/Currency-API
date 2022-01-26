from django.contrib import admin
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

from . import views


urlpatterns = [
    path('', views.index),
    path('car', views.add_car),
    path('<str:car_name>', views.get_car),
]
