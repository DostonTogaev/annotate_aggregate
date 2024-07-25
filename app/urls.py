from django.contrib import admin
from django.urls import path, include
from app.views import product
urlpatterns = [
    path('', product, name='index'),
]