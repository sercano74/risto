from django.contrib import admin
from django.urls import path
from . import views

app_name = 'App01Menus'

urlpatterns = [
    
    path('Menu/', views.Menu, name='Menu'),
    path('detail/<int:pk>', views.productDetail, name='productDetail'),
]