import uuid
from django.db import models
from inventory.fields import AutoCreatedField, AutoLastModifiedField
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    class Meta:
        abstract = True


class Keg(TimeStampedModel):
    """
    Represents a re-usable keg in the warehouse
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # The unique id of the keg
    litres = models.IntegerField(choices=[(
        50, '50 Litres'), (30, '30 Litres'), (20, '20 Litres')], default=50)

    def __str__(self):
        return "{}".format(str(self.id))

    class Meta:
        verbose_name = "keg"
        verbose_name_plural = "kegs"
        ordering = ('created',)


class Fill(TimeStampedModel):
    """
    Represents an instance of beer from a batch, within a keg
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # The unique id of the keg
    keg = models.ForeignKey(
        'inventory.Keg', related_name='keg')
    batch = models.ForeignKey(
        'inventory.Batch', related_name='batch')

    def __str__(self):
        return "{}L - {}".format(str(self.keg.litres), str(self.batch.beer.name))

    class Meta:
        verbose_name = "keg fill"
        verbose_name_plural = "keg fills"
        ordering = ('created',)


class Batch(TimeStampedModel):
    """
    Represents a completed batch of beer
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # The unique id of the batch
    litres = models.IntegerField(default=1000)
    beer = models.ForeignKey('inventory.Beer', related_name='beer', null=True)

    def __str__(self):
        return "{} - {}".format(str(self.beer.name), str(self.created))

    class Meta:
        verbose_name = "batch"
        verbose_name_plural = "batches"
        ordering = ('created',)


class Beer(TimeStampedModel):
    """
    Represents a variety of beer that is produced
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # The unique id of the beer
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(str(self.name))

    class Meta:
        verbose_name = "beer"
        verbose_name_plural = "beers"
        ordering = ('created',)
