# Generated by Django 4.2 on 2024-08-24 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0024_alter_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["category", "description"],
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["product", "description", "category", "price"],
                "permissions": [
                    ("can_edit_category", "Can edit category"),
                    ("can_edit_description", "Can edit description"),
                    ("can_edit_is_published", "Can edit is_published"),
                ],
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.AlterModelOptions(
            name="version",
            options={"verbose_name": "version", "verbose_name_plural": "versions"},
        ),
        migrations.AlterField(
            model_name="category",
            name="category",
            field=models.CharField(max_length=100, verbose_name="Category"),
        ),
        migrations.AlterField(
            model_name="category",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="category",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="catalog.category",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="catalog/image", verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="IsPublished"),
        ),
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Please indicate the owner of the ad",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Owner",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(verbose_name="Price"),
        ),
        migrations.AlterField(
            model_name="product",
            name="product",
            field=models.CharField(max_length=100, verbose_name="Product"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Updated At"),
        ),
        migrations.AlterField(
            model_name="product",
            name="view_counter",
            field=models.PositiveIntegerField(
                default=0, editable=False, verbose_name="Counter views"
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="is_current",
            field=models.BooleanField(default=True, verbose_name="Is current"),
        ),
        migrations.AlterField(
            model_name="version",
            name="number",
            field=models.PositiveIntegerField(verbose_name="Version number"),
        ),
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.product",
                verbose_name="Product",
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Title"),
        ),
    ]