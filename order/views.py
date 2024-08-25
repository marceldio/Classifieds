from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from catalog.models import Product
from order.models import Order
from order.services import send_order_email


class OrderCreateView(CreateView):
    model = Order
    fields = ('product', 'name', 'email','message',)

    def get_success_url(self):
        return reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['name'] = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        obj = form.save()
        send_order_email(obj)
        return super().form_valid(form)
