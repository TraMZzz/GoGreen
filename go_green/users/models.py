# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    name = models.CharField(_('Name of User'), blank=True, max_length=255, unique=True)
    clean_count = models.PositiveIntegerField(_('Clean rating'), default=0)
    status = models.CharField(_('Status'), blank=True, max_length=55)

    is_volunteer = models.BooleanField(_('Volunteer ?'), default=False)
    volunteer_group_name = models.CharField(_('Volunteer Group Name'), blank=True, max_length=100)

    show_contact = models.BooleanField(_('Show Contact ?'), default=True)
    contact_email = models.EmailField(_('Contact email'), max_length=254, blank=True)
    contact_phone = models.CharField(_('Contact phone'), blank=True, max_length=100)
    contact_url = models.URLField(_('Contact url'), blank=True, max_length=100)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
