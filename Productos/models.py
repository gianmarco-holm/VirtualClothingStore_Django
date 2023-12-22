from django.db import models
from django.db.models import Sum

class Category(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class Color(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color

class Size(models.Model):
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.size

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def total_stock(self):
        total_stock = Stock.objects.filter(product=self).aggregate(Sum('quantity'))['quantity__sum']
        return total_stock if total_stock else 0

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.color.color} - {self.size.size}"
