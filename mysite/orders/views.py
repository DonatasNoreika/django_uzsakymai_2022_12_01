from django.shortcuts import render
from django.views import generic
from .models import MyOrder
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class OrderListView(generic.ListView):
    model = MyOrder
    context_object_name = "orders"
    template_name = "orders.html"


class UserOrderListView(LoginRequiredMixin, generic.ListView):
    model = MyOrder
    context_object_name = "orders"
    template_name = "user_orders.html"

    def get_queryset(self):
        return MyOrder.objects.filter(user=self.request.user)

class UserOrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = MyOrder
    context_object_name = "order"
    template_name = "user_order.html"
