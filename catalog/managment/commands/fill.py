from catalog.models import Product
from django.core.management import BaseCommand


class Command(BaseCommand):
    products_data = [{'name': 'NZXT'}, {'description': ''},
                     {'name': 'Deepcool'}, {'description': ''},
                     {'name': 'Phantecs'}, {'description': ''},
                     {'name': 'Termaltake'}, {'description': ''},
                     {'name': 'Lenovo'}, {'description': ''},
                     ]
    for product_item in products_data:
        Product.objects.create(**product_item)