from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from django.views import View
from .models import Product
from utils.response import ResponseDto

import json


@method_decorator(csrf_exempt, name='dispatch')
class ProductsView(View):
    def get(self, request, id=None):
        try:
            if id:
                product = get_object_or_404(Product, pk=id)
                response_data = {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'image': product.image
                }
                response = ResponseDto(data=response_data)
                return response.to_json()
            else:
                products = Product.objects.all()
                response_data = []
                for product in products:
                    product_data = {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'price': product.price,
                        'image': product.image
                    }
                    response_data.append(product_data)
                response = ResponseDto(data=response_data)
                return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()

    @csrf_exempt
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            price = data.get('price')
            image = data.get('image')
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                image=image
            )
            response = ResponseDto(message="Created", data=product)
            return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()

    def put(self, request, id=None):
        try:
            product = Product.objects.get(pk=id)
            data = json.loads(request.body)
            product.name = data.get('name') or product.name
            product.description = data.get('description') or product.description
            product.price = data.get('price') or product.price
            product.image = data.get('image') or product.image
            product.save()

            response = ResponseDto(message="Updated", data={
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'image': product.image
            })
            return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()

    def delete(self, request, id=None):
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            response = ResponseDto(message="Deleted")
            return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()


@staticmethod
def as_view():
    return csrf_exempt(ProductsView().dispatch)
