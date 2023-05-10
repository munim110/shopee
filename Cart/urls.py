from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>', remove_from_cart, name='remove_from_cart'),
    path('update/<int:cart_item_id>', update_cart, name='update_cart'),
    path('increase/<int:cart_item_id>', increase_quantity, name='increase_quantity'),
    path('decrease/<int:cart_item_id>', decrease_quantity, name='decrease_quantity'),
    path('checkout/', checkout, name='checkout'),
    path('order/<int:order_id>', order_detail, name='order'),
]