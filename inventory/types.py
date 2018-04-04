import graphene
from graphene_django import DjangoObjectType
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
