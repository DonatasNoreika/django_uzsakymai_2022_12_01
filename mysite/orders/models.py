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

    def total(self):
        total = 0
        lines = self.lines.all()
        for line in lines:
            total += line.product.price * line.quantity
        return total

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.date} ({self.user}) - {self.status}"

class OrderLine(models.Model):
    order = models.ForeignKey("MyOrder", on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField("Kiekis")

    def sum(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.order} ({self.product}) - {self.quantity}"
