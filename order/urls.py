from django.urls import path

from order.apps import OrderConfig
from order.views import OrderCreateView

app_name = OrderConfig.name

urlpatterns = [
    path('order/<int:pk>/', OrderCreateView.as_view(), name='order'),
    ]