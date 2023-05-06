from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product/all_products.html', {'products': products, 'categories': categories})


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found')
    return render(request, 'product/product_detail.html', {'product': product})
