from django.shortcuts import render
from django.views import generic
from .models import MyOrder, OrderLine
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from .forms import OrderCreateForm

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

class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = MyOrder
    fields = ['status']
    success_url = "/user_orders/"
    template_name = 'order_form.html'
    # form_class = OrderCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class LineCreateView(LoginRequiredMixin, generic.CreateView):
    model = OrderLine
    fields = ['product', 'quantity']
    template_name = 'orderline_form.html'

    def get_success_url(self):
        return reverse('user_order', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.order = MyOrder.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)