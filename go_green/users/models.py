# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .fields import JSONField
from go_green.badge.models import Badge


@python_2_unicode_compatible
class User(AbstractUser):

    clean_count = models.PositiveIntegerField(_('Clean rating'), default=0)
    status = models.CharField(_('Status'), blank=True, max_length=55)

    badges = models.ManyToManyField(Badge, _('badges'), db_table='users_badges', blank=True)
    is_volunteer = models.BooleanField(_('Volunteer ?'), default=False)
    volunteer_group_name = models.CharField(_('Volunteer Group Name'), blank=True, max_length=100)

    show_contact = models.BooleanField(_('Show Contact ?'), default=True)
    contact_email = models.EmailField(_('Contact email'), max_length=254, blank=True, null=True)
    contact_phone = models.CharField(_('Contact phone'), blank=True, max_length=100)
    contact_url = models.URLField(_('Contact url'), blank=True, max_length=100)

    uid = models.CharField(verbose_name=_('uid'), max_length=200, unique=True)
    extra_data = JSONField(verbose_name=_('extra data'), default=dict)
    token = models.TextField(
        blank=True,
        verbose_name=_('token provider'))
    expires_at = models.DateTimeField(blank=True, null=True,
                                      verbose_name=_('expires at'))

    class Meta:
        unique_together = ('uid', 'token')

    def __str__(self):
        return self.username
