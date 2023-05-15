from django.test import TestCase
from graphene.test import Client

from Products.schema import schema as schema_products


class ProductsTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema_products)

    def test_create_products(self):
        query = '''
            mutation {
                createProduct(
                    name: "Product 1"
                    description: "Description 1"
                    price: 100,
                    image: "https://www.google.com"
                ) {
                    product {
                        id
                        name
                        description
                        price
                        image
                    }
                }
            }
        '''

        expected = {
            'createProduct': {
                'product': {
                    'name': 'Product 1',
                    'description': 'Description 1',
                    'price': 100.0,
                    'image': 'https://www.google.com'
                    
                }
            }
        }

        executed = self.client.execute(query)
        print(executed)
        self.assertEqual(executed, expected)


