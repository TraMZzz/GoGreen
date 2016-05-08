# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from go_green.users.models import User
from go_green.image.models import Image


@python_2_unicode_compatible
class Event(models.Model):
    POLLUTION_CHOICES = (
        ('normal', _('Slightly littered')),
        ('bad', _('Extremely trashy')),
        ('extbad', _('Garbocalipse'))
    )
    EQUIPMENT_CHOICES = (
        ('me', _('Me')),
        ('all', _('Every for himself'))
    )
    GARBAGE_CHOICES = (
        ('yes', _('Yes')),
        ('no', _('No'))
    )
    FOOD_CHOICES = (
        ('yes', _('Yes')),
        ('no', _('No'))
    )
    creator = models.ForeignKey(User, verbose_name=_('Creator'),
                                related_name='events')
    collaborators = models.ManyToManyField(User, _('collaborators'),
                                           db_table='event_collaborators', blank=True)
    name = models.CharField(_('Event name'), max_length=50)
    description = models.CharField(_('Event description'), max_length=255)
    location = models.PointField(max_length=40, null=True)
    prefered_radius = models.IntegerField(default=1, help_text="in kilometers")

    start_time = models.DateTimeField(_('Start time'), blank=True, null=True)
    pollution_level = models.CharField(_('Pollution level'), max_length=6,
                                       choices=POLLUTION_CHOICES, default='normal')
    equipment = models.CharField(_('Who provides equipment ?'), max_length=6,
                                 choices=EQUIPMENT_CHOICES, default='all')
    garbage = models.CharField(_('Is the garbage take-out arranged for ?'),
                               max_length=6,
                               choices=GARBAGE_CHOICES, default='no')
    food = models.CharField(_('Is food provided?'), max_length=6,
                            choices=FOOD_CHOICES, default='no')

    image_before = models.ManyToManyField(Image, _('Before'), db_table='event_images_before', blank=True)
    image_after = models.ManyToManyField(Image, _('After'), db_table='event_images_after', blank=True)

    is_cleaned = models.BooleanField(_('Cleaned ?'), default=False)

    objects = models.GeoManager()

    def __str__(self):
        return self.name
