from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    sku  = models.CharField(max_length=50)
    UPC_number = models.CharField(max_length=50, null=True)
    Price = models.IntegerField(null=True)
    Description = models.TextField(null=True)
    image =models.ImageField(upload_to='uploads/',null=True)
