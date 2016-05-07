# -*- coding: utf-8 -*-

from rest_framework import serializers

from go_green.users.serializers import UserViewSetSerializer
from go_green.image.serializers import ImageViewSetSerializer

from .models import Event


class EventViewSetSerializer(serializers.ModelSerializer):
    creator = UserViewSetSerializer(read_only=True)
    collaborators = UserViewSetSerializer(many=True, read_only=True)
    image_before = ImageViewSetSerializer(many=True, read_only=True)
    image_after = ImageViewSetSerializer(many=True, read_only=True)

    class Meta:
        model = Event
