from rest_framework import serializers
from inventory.models import Fill, Keg, Batch, Beer


class BeerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beer
        fields = ('name',)


class BatchSerializer(serializers.ModelSerializer):
    beer = BeerSerializer(read_only=True)

    class Meta:
        model = Batch
        fields = ('id', 'litres', 'beer', 'created')


class KegSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, keg):
        try:
            return Fill.objects.get(keg=keg.id).batch.beer.name
        except:
            return None

    class Meta:
        model = Keg
        fields = ('id', 'litres', 'status', 'created')


class FillSerializer(serializers.ModelSerializer):
    keg = KegSerializer(read_only=True)
    batch = BatchSerializer(read_only=True)

    class Meta:
        model = Fill
        fields = ('keg', 'batch', 'created')
