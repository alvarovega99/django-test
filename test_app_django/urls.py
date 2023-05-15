from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
##importar schema
from Products.schema import schema as schema_products
from Users.schema import schema as schema_users


urlpatterns = [
    path('graphql/products', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_products))),
    path('graphql/users', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema_users))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
