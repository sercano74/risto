from django.contrib import admin
from django.urls import path
from . import views

app_name = 'App01Menus'

urlpatterns = [
    
    path('menu/', views.menu, name='menu'),
    path('detail/<int:pk>', views.productdetail, name='productdetail'),
]