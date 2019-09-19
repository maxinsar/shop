from django.urls import path
from .views import products, product

urlpatterns = [
    path('products/', products, name = "products"),
    path('product/<slug:slug>', products, name = "product"),
]
