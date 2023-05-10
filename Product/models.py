from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', default='product_images/default.png')
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


rating_choices = (
    (1, '1 - Poor'),
    (2, '2 - Fair'),
    (3, '3 - Average'),
    (4, '4 - Good'),
    (5, '5 - Excellent'),
)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=rating_choices, default=3)