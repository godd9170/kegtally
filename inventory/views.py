from rest_framework import viewsets, views, response, status
from inventory.models import Fill, Keg, Batch
from inventory.serializers import FillSerializer, KegSerializer, BatchSerializer
from django.http import Http404
from common.models import QuickbooksCredentials
from quickbooks import Oauth2SessionManager, QuickBooks
from quickbooks.objects.item import Item


class Batches(viewsets.ViewSet):
    """
    API endpoint that shows all currently available batches.
    """

    def list(self, request):
        batches = Batch.objects.all()
        serializer = BatchSerializer(batches, many=True)
        return response.Response(serializer.data)


class Fills(viewsets.ViewSet):
    """
    API endpoint that shows all currently filled kegs.
    """

    def list(self, request):
        fills = Fill.objects.all()
        serializer = FillSerializer(fills, many=True)
        return response.Response(serializer.data)


class KegDetail(views.APIView):
    """
    Returns a keg given it's id
    """

    def get_object(self, uuid):
        try:
            return Keg.objects.get(pk=uuid)
        except:
            raise Http404

    def get(self, request, uuid, format=None):
        keg = self.get_object(uuid)
        serializer = KegSerializer(keg)
        return response.Response(serializer.data)

    def put(self, request, uuid, format=None):
        keg = self.get_object(uuid)
        batch = Batch.objects.get(pk=request.data['batch'])
        fill = Fill(batch=batch, keg=keg)
        fill.save(force_insert=True)
        creds = QuickbooksCredentials.objects.all().first()

        # Get a session
        self.session_manager = Oauth2SessionManager(
            sandbox=True,
            client_id=creds.clientId,
            client_secret=creds.clientSecret,
            access_token=creds.accessToken,
        )

        # Get a client
        client = QuickBooks(
            sandbox=True,
            session_manager=self.session_manager,
            company_id=creds.realmId
        )

        # eff shit up
        item = Item.get(batch.beer.qbid, qb=client)
        item.QtyOnHand = 1
        item.save(qb=client)
        return response.Response(status.HTTP_200_OK)


class FillBill(views.APIView):
    """
    Update a fill as sold
    """

    def post(self, request, uuid, format=None):
        creds = QuickbooksCredentials.objects.first()

        # Get a session
        self.session_manager = Oauth2SessionManager(
            sandbox=True,
            client_id=creds.clientId,
            client_secret=creds.clientSecret,
            access_token=creds.accessToken,
        )

        # Get a client
        client = QuickBooks(
            sandbox=True,
            session_manager=self.session_manager,
            company_id=creds.realmId
        )

        # eff shit up
        item = Item.filter(id=request, qb=client)
        print('>>>>>>>>>>>>>>CUSTOMERS>>>>>>>>>>>>..', item.__str__)
