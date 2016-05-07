# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from go_green.users.models import User
from go_green.image.models import Image


@python_2_unicode_compatible
class Event(models.Model):
    creator = models.ForeignKey(User, verbose_name=_('Creator'),
                                related_name='events')
    collaborators = models.ManyToManyField(User, _('collaborators'),
                                           db_table='event_collaborators', null=True)
    name = models.CharField(_('Event name'), max_length=50)
    description = models.CharField(_('Event description'), max_length=255)
    location = models.PointField(max_length=40, null=True)
    prefered_radius = models.IntegerField(default=1, help_text="in kilometers")

    image_before = models.ManyToManyField(Image, _('Before'), db_table='event_images_before')
    image_after = models.ManyToManyField(Image, _('After'), db_table='event_images_after')

    objects = models.GeoManager()

    def __str__(self):
        return self.name
