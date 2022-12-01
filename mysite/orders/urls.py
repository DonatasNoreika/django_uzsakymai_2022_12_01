"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderListView.as_view(), name='orders'),
    path("user_orders/", views.UserOrderListView.as_view(), name='user_orders'),
    path("user_orders/<int:pk>", views.UserOrderDetailView.as_view(), name='user_order'),
    path("user_orders/<int:pk>/update", views.UserOrderUpdateView.as_view(), name='user_order_update'),
    path("user_orders/<int:pk>/delete", views.UserOrderDeleteView.as_view(), name='user_order_delete'),
    path("user_orders/new", views.OrderCreateView.as_view(), name='order_new'),
    path("user_orders/<int:pk>/neworderline", views.LineCreateView.as_view(), name='neworderline'),
]
