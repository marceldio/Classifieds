# Generated by Django 5.0.6 on 2024-08-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
    ]
