from django.db import models
from django.utils.translation import ugettext_lazy as _


class DynamicSetting(models.Model):

    SETTING_TYPES = (
        1, _(u'Boolean'),
        2, _(u'Integer'),
        3, _(u'Decimal'),
        4, _(u'Text')
    )

    name = models.CharField(max_length=255, null=False, blank=False)