from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def cart(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    try:
        user_cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        user_cart = Cart.objects.create(user=request.user)
        user_cart.save()
    items = user_cart.items.all()
    return render(request, 'cart/cart.html', {'cart': user_cart, 'items': items})


def add_to_cart(request, product_id):
    user_cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    user_cart.add_item(product, 1)
    return redirect(cart)


def remove_from_cart(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    user_cart.remove_item(cart_item_id)
    return redirect(cart)


def update_cart(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    quantity = request.POST['quantity']
    user_cart.update_item(cart_item_id, quantity)
    return redirect(cart)


def increase_quantity(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    user_cart.increase_quantity(cart_item_id)
    return redirect(cart)


def decrease_quantity(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    user_cart.decrease_quantity(cart_item_id)
    return redirect(cart)


def checkout(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    user_cart = Cart.objects.get(user=request.user)
    items = user_cart.items.all()
    if request.method == 'POST':
        address = request.POST['address']
        phone = request.POST['phone']
        new_order = Order.objects.create(user=request.user, address=address, phone=phone)
        new_order.items.set(items)
        new_order.set_total()
        new_order.save()
        user_cart.items.clear()
        user_cart.set_total()
        user_cart.save()
        return redirect('order', order_id=new_order.id)

    return render(request, 'cart/checkout.html', {'cart': user_cart, 'items': items,
                                                   'total': user_cart.total, 'user': request.user})


def order_detail(request, order_id):
    if not request.user.is_authenticated:
        return redirect('signup')
    order = Order.objects.get(id=order_id)
    items = order.items.all()
    return render(request, 'cart/order_detail.html', {'order': order, 'items': items, 'total': order.total})



