from django.conf import settings
from django.core.mail import send_mail

from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        'Заявка на покупку ',
        f'{order_item.name} ({order_item.email}) ordering: {order_item.product.name}.'
        f'Вот сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.product.owner.email]
    )
