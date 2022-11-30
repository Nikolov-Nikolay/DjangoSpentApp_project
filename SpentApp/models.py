from django.db import models

# Create your models here.


class Product(models.Model):
    ProductId = models.IntegerField(primary_key=True, null=False)
    ProductName = models.CharField(max_length=500)
    ProductAmount = models.IntegerField()
    ProductPrice = models.IntegerField()
    ProductTotalPrice = models.IntegerField()
    Date = models.DateField()
    