from django.db import models
import random
from django.contrib.auth.models import User
from PIL import Image

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=100)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
       return self.user.username if self.user else "No Username"

class Farmer_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='farmer_profilepic')

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height>250 or img.width>250:
            output_size =(250,250)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=8, unique=True)
    product_name = models.CharField(max_length=250, blank=False)  
    product_description = models.TextField(blank=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_shipping_address = models.TextField(blank=False)
    product_image = models.ImageField(default='default_product.jpg', upload_to='product_image', blank=False)
    quantity = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f"{self.product_name} by {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.product_id:  
            self.product_id = self.generate_product_id()
        super(Products, self).save(*args, **kwargs)

        img = Image.open(self.product_image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.product_image.path)
    @staticmethod
    def generate_product_id():
        """Generate a unique 8-digit product ID"""
        return str(random.randint(10000000, 99999999))





