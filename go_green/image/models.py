# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Image(models.Model):
    name = models.CharField(_('Image name'), max_length=100)
    image = models.ImageField(upload_to="event_image")

    def __str__(self):
        return self.name
