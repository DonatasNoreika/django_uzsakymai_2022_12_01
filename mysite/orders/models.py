from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    name = models.CharField("Pavadinimas", max_length=200)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField("Pavadinimas", max_length=200)
    price = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.name} ({self.price})"

class MyOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField("Data", auto_now_add=True)

    def __str__(self):
        return f"{self.date} ({self.user}) - {self.status}"

class OrderLine(models.Model):
    order = models.ForeignKey("MyOrder", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField("Kiekis")

    def __str__(self):
        return f"{self.order} ({self.product}) - {self.quantity}"
