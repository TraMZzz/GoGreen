# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Badge(models.Model):
    name = models.CharField(_('Image name'), max_length=250, unique=True)
    icon = models.ImageField(upload_to="bange_icon")

    def __str__(self):
        return self.name
