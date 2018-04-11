import uuid
from django.db import models
from common.models import TimeStampedModel


class Customer(TimeStampedModel):
    """
    Represents a customer
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # The unique id of customer
    name = models.CharField(max_length=100)
    # Link to the quickbooks parent item Id
    qbid = models.IntegerField(null=True)

    def __str__(self):
        return "{}".format(str(self.name))

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ('created',)
