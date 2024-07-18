from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    UPC_number = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    confidence = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

class ProductImage(models.Model):
    image = models.ImageField(null=True, upload_to='image/')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
