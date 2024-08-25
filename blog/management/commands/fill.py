from django.core.management.base import BaseCommand
from blog.models import Blog
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_products():
        with open('blog.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            products = [item for item in data if item['model'] == 'blog.blog']
        return products

    def handle(self, *args, **options):
        # Удалите все продукты
        Blog.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_fields = product['fields']
            product_for_create.append(
                Blog(
                    pk=product['pk'],
                    title=product_fields['title'],
                    content=product_fields['content'],
                    image=product_fields['image'],

                    created_at=product_fields['created_at'],
                    updated_at=product_fields['updated_at'],
                    owner=product_fields['owner']
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Blog.objects.bulk_create(product_for_create)
