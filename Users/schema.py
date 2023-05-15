import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    @login_required
    def resolve_users(self, info, **kwargs):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, name, email, password):
        user = User(name=name, email=email, password=password)
        user.save()
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    @login_required
    def mutate(self, info, id, name=None, email=None, password=None):
        user = User.objects.get(pk=id)
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        user.save()
        return UpdateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)