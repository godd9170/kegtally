import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q
from inventory.models import Keg, Fill, Batch, Beer


class KegType(DjangoObjectType):
    class Meta:
        model = Keg


class FillType(DjangoObjectType):
    class Meta:
        model = Fill


class BatchType(DjangoObjectType):
    class Meta:
        model = Batch


class BeerType(DjangoObjectType):
    class Meta:
        model = Beer


class Query(graphene.ObjectType):
    kegs = graphene.List(KegType)
    fills = graphene.List(FillType)
    batches = graphene.List(BatchType)
    beers = graphene.List(BeerType)

    def resolve_kegs(self, info, **kwargs):
        return Keg.objects.all()

    def resolve_fills(self, info, **kwargs):
        return Fill.objects.all()

    def resolve_batches(self, info, **kwargs):
        return Batch.objects.all()

    def resolve_beers(self, info, **kwargs):
        return Beer.objects.all()
