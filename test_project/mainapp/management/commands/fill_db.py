from django.core.management.base import BaseCommand
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser
from configparser import RawConfigParser
from django.conf import settings

import json, os

JSON_PATH = 'mainapp/json'

local_config_path = os.path.join(settings.BASE_DIR, 'config', 'local.conf')
config = RawConfigParser()
config.read(local_config_path)


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='UTF-8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.all().delete()




        ShopUser.objects.create_superuser(config.get("admin", "admin_username"), config.get("admin", "admin_email"),\
                                          config.get("admin", "admin_password"), config.get("admin", "admin_age"))

        """super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)"""