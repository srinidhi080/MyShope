from django.db import models


class productlist(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image =models.CharField(max_length=2086)