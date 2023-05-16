from django.urls import path
from .views import ProductsView


urlpatterns = [
    path('product/', ProductsView.as_view(), name='product-list'),
    path('product/<int:id>', ProductsView.as_view(), name='product-detail'),
]