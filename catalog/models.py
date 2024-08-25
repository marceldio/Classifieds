from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(
        max_length=100,
        verbose_name="category"
    )
    description = models.TextField(
        **NULLABLE,
        verbose_name="description"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="updated at")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["category", "description"]

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="name",
        default="Ad"
    )
    description = models.TextField(
        verbose_name="description",
        **NULLABLE
    )
    slug = models.CharField(
        max_length=200,
        verbose_name='slug',
        **NULLABLE
    )
    image = models.ImageField(
        upload_to="catalog/image",
        verbose_name="image",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="category",
        **NULLABLE,
        related_name="products"
    )
    price = models.PositiveIntegerField(verbose_name="price")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created At")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="updated At")
    is_published = models.BooleanField(default=False, verbose_name="is_published")
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="counter views",
        editable=False
    )
    owner = models.ForeignKey(
        User, verbose_name="owner",
        help_text="Please indicate the owner of the ad",
        **NULLABLE,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ["name", "description", "category", "price"]
        permissions = [
            ("can_edit_category", "Can edit category"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_is_published", "Can edit is_published")]

    def __str__(self):
        return f'{self.name}'


class Version(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    number = models.PositiveIntegerField(verbose_name='version number')
    is_current = models.BooleanField(default=False, verbose_name='is current')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
