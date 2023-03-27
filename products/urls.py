from django.urls import path
from . import views


# Adjust for products
urlpatterns = [
    path ('', views.cars_list),
    path ('<int:pk>/', views.car_detail),
    path ('<str:make>/', views.cars_by_make)
]