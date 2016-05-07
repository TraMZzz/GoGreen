# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Image


class ImageViewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
