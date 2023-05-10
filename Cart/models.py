from django.db import models
from Product.models import Product
from django.contrib.auth.models import User

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
    
    def get_total(self):
        return self.product.price * self.quantity
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f'{self.user.username} - {self.total}'
    
    def set_total(self):
        self.total = 0
        for item in self.items.all():
            self.total += item.get_total()
        self.save()
    
    def add_item(self, product, quantity):
        cart_item = CartItem.objects.create(product=product, quantity=quantity)
        self.items.add(cart_item)
        self.set_total()

    def remove_item(self, cart_item_id):
        cart_item = CartItem.objects.get(id=cart_item_id)
        self.items.remove(cart_item)
        self.set_total()

    def update_item(self, cart_item_id, quantity):
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()
        self.set_total()

    def increase_quantity(self, cart_item_id):
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity += 1
        cart_item.save()
        self.set_total()

    def decrease_quantity(self, cart_item_id):
        cart_item = CartItem.objects.get(id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            self.remove_item(cart_item_id)
        cart_item.save()
        self.set_total()

    def clear(self):
        self.items.clear()
        self.set_total()




order_status = (
    ('Order Received', 'Order Received'),
    ('Order Processing', 'Order Processing'),
    ('On the way', 'On the way'),
    ('Order Completed', 'Order Completed'),
    ('Order Cancelled', 'Order Cancelled'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_status = models.CharField(max_length=50, choices=order_status, default='Order Received')
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f'{self.user.username} - {self.total}'
    
    def set_total(self):
        self.total = 0
        for item in self.items.all():
            self.total += item.get_total()
        self.save()

    def add_item(self, product, quantity):
        cart_item = CartItem.objects.create(product=product, quantity=quantity)
        self.items.add(cart_item)
        self.set_total()

    def update_order_status(self, order_status):
        self.order_status = order_status
        self.save()

    

