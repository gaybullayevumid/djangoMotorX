from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to="post-images")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    reviews = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    mileage = models.DecimalField(max_digits=6, decimal_places=1)
    transmission = models.CharField(max_length=50)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)    

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    table = models.CharField(max_length=100)
    time = models.CharField(max_length=100)