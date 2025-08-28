import requests
from django.utils.text import slugify
from django.core.management import BaseCommand

from product.models import Category, Product
from pyexpat import features


class Command(BaseCommand):
        def handle(self, *args, **options):
            print("Creating data.............")
        response=requests.get("https://fakestoreapi.com/products").json()

        for product in response:
            category,_ = Category.objects.get_or_create(
                title=product["category"],
                slug=slugify(product["category"]),
                featured=True

            )
            product = Product.objects.create(
                category=category,
                title=product["title"],
                slug=slugify(product["title"]),
                price=product["price"],
                thumbnail=product["image"],
                description=product["description"]

            )

        print("Insert Complete")

