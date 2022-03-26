import requests
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify 
from django.db import transaction

from django.conf import settings
from product.models import Product, ProductCategory

class Command(BaseCommand):
    help = 'Import Bring! catalog into food from JSON file.'

    def add_arguments(self, parser):
        parser.add_argument("--replace", default=False, required=False, type=bool)
        parser.add_argument("--run", default=False, required=False, type=bool)
        parser.add_argument("--force", default=False, required=False, type=bool)

    def handle(self, *args, replace, run, force, **options):
        if not run:
            print("This script is running as a dry run and will be rolled back at the end leaving no database changes.\n\n")
        elif not force:
            should_continue = input("This script is NOT a dry run and will make database changes when it is run, continue? [y/N]:")
            if should_continue.lower() != "y":
                return

        response = requests.get(settings.BRING_API_CATALOG_ENDPOINT)
        bring_catalog = response.json()["catalog"]

        try:
            with transaction.atomic():
                if replace:
                    print("This script deletes all products and categories prior to running for a fresh start!")
                    products_to_be_deleted = Product.objects.filter(imported_at__isnull=False)
                    product_categories_to_be_deleted = ProductCategory.objects.filter(imported_at__isnull=False)

                    print(f"{products_to_be_deleted.count()} products and {products_to_be_deleted.count()} product categories to be deleted.")
                    products_to_be_deleted.delete()
                    product_categories_to_be_deleted.delete()

                for section in bring_catalog["sections"]:
                    print(section['name'], f"{len(section['items'])} products.")

                    product_category, created = ProductCategory.objects.get_or_create(
                        name=section['name'],
                        defaults = {
                            "slug": slugify(section['name']),
                            "imported_at": timezone.now()
                        }
                    )
                    products = [
                        Product(
                            name=item['name'],
                            slug=slugify(item['name']),
                            bring_id=item['itemId'],
                            category=product_category,
                            imported_at=timezone.now()
                        )
                        for item in section['items']
                    ]

                    Product.objects.bulk_update_or_create(products, ['category', 'name', 'slug'], match_field='bring_id')

                    if not run:
                        raise Exception("Rolling back because script was run as a dry run.")
        except Exception:
            raise Exception
        