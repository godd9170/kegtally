from rest_framework import viewsets, views, response
from inventory.models import Fill
from inventory.serializers import FillSerializer


class Fills(viewsets.ViewSet):
    """
    API endpoint that shows all currently filled kegs.
    """

    def list(self, request):
        fills = Fill.objects.all()
        serializer = FillSerializer(fills, many=True)
        return response.Response(serializer.data)
