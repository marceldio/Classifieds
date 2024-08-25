from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    tg_name = models.CharField(max_length=50, verbose_name='Telegram nickname', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Country', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Avatar', **NULLABLE)

    token = models.CharField(max_length=255, verbose_name='token', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
