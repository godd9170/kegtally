import uuid
from django.db import models
from common.models import TimeStampedModel


class Customer(TimeStampedModel):
    """
    Represents an Customer in Quickbooks
    """
    qbid = models.IntegerField(primary_key=True, editable=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(str(self.qbid))

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ('created',)
