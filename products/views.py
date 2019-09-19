from django.shortcuts import render
from .models import Category, Product


def products(request):
    categories = Category.objects.all()
    products = Product.objects.filter(aviable=True)
    return render(request, 'shop/products.html',
    {'categories':categories,
     'products':products})


def product(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'shop/product.html', {'product':product})
