
import graphene
import uuid
from inventory.models import Keg, Fill, Batch, Beer
from inventory.types import KegType, FillType, BatchType, BeerType


class CreateKeg(graphene.Mutation):
    id = graphene.String()
    tag = graphene.String()
    litres = graphene.Int()

    class Arguments:
        tag = graphene.String()
        litres = graphene.Int()

    def mutate(self, info, tag, litres):

        keg = Keg(
            id=uuid.uuid4(),
            tag=tag,
            litres=litres
        )
        keg.save()

        return CreateKeg(
            id=keg.id,
            tag=keg.tag,
            litres=keg.litres
        )
