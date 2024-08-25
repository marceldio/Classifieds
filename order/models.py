from django.db import models

class Order(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)

    name = models.CharField(max_length=150, verbose_name='name', blank=True)
    email = models.EmailField(max_length=150, verbose_name='email')
    message = models.TextField(verbose_name='message')

    closed = models.BooleanField(default=False, verbose_name='closed', blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order to: {self.product} from {self.email}'


    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['-created']

