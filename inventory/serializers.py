from rest_framework import serializers
from inventory.models import Fill, Keg, Batch, Beer


class KegSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keg
        fields = ('id', 'litres', 'created')


class BeerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beer
        fields = ('name',)


class BatchSerializer(serializers.ModelSerializer):
    beer = BeerSerializer(read_only=True)

    class Meta:
        model = Batch
        fields = ('litres', 'beer', 'created')


class FillSerializer(serializers.ModelSerializer):
    keg = KegSerializer(read_only=True)
    batch = BatchSerializer(read_only=True)

    class Meta:
        model = Fill
        fields = ('keg', 'batch', 'created')
