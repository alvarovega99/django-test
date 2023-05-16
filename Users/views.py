from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from django.views import View
from .models import User
from utils.response import ResponseDto

import json


@method_decorator(csrf_exempt, name='dispatch')
class UsersView(View):
    def get(self, request, id=None):
        try:
            if id:
                user = get_object_or_404(User, pk=id)
                response_data = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'password': user.password,
                }
                response = ResponseDto(data=response_data)
                return response.to_json()
            else:
                users = User.objects.all()
                response_data = []
                for user in users:
                    user_data = {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'password': user.password,
                    }
                    response_data.append(user_data)
                response = ResponseDto(data=response_data)
                return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()
        
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            image = data.get('image')
            user = User.objects.create(
                name=name,
                email=email,
                password=make_password(password),
            )
            response = ResponseDto(message="Created", data={
                'id': user.id,
                'name': user.name,
                'email': user.email,
            })
            return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()
        
    def put(self, request, id=None):
        try:
            user = User.objects.get(pk=id)
            data = json.loads(request.body)
            user.name = data.get('name') or user.name
            user.email = data.get('email') or user.email
            user.password = data.get('password') or user.password
            user.save()

            response = ResponseDto(message="Updated", data={
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password,
            })
            return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()
        
    def delete(self, request, id=None):
        try:
            user = User.objects.get(pk=id)
            user.delete()
            response = ResponseDto(message="Deleted")
            return response.to_json()
        except Exception as e:
            response = ResponseDto(status=500, message=str(e))
            return response.to_json()