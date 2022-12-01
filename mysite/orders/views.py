from django.shortcuts import render
from django.views import generic
from .models import MyOrder

# Create your views here.
class OrderListView(generic.ListView):
    model = MyOrder
    context_object_name = "orders"
    template_name = "orders.html"


