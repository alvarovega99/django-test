import graphene
from graphene_django import DjangoObjectType

from .models import Product

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "image")

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product = graphene.Field(ProductType, id=graphene.Int(required=True))

    def resolve_products(self, info):
        return Product.objects.all()

    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)
    

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)
        image = graphene.String(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, description, price, image):

        product = Product(name=name, description=description, price=price, image=image)
        product.save()
        return CreateProduct(product=product)
    
class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        description = graphene.String()
        price = graphene.Float()
        image = graphene.String()

    product = graphene.Field(ProductType)

    def mutate(self, info, id, name=None, description=None, price=None, image=None):

        product = Product.objects.get(pk=id)
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if image:
            product.image = image
        product.save()
        return UpdateProduct(product=product)
    

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, id):

        product = Product.objects.get(pk=id)
        product.delete()
        return DeleteProduct(product=product)
    

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)