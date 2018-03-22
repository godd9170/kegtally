from django.db import models
from common.fields import AutoCreatedField, AutoLastModifiedField
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


class QuickbooksCredentials(models.Model):
    """
    Here we store QB Access Tokens
    """
    name = models.CharField(max_length=100)
    clientId = models.TextField()
    clientSecret = models.TextField()
    realmId = models.TextField()
    authorizationCode = models.TextField()
    accessToken = models.TextField(blank=True, default=None, null=True)

    class Meta:
        verbose_name = "quickbooks credentials"
        verbose_name_plural = "quickbooks credentials"
