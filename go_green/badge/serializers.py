# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Badge


class BadgeViewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
