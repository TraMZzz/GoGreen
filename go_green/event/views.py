# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from geopy.geocoders import Nominatim

from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import (
    exceptions, filters, mixins, pagination,
    permissions, serializers, status, viewsets)

from .models import Event
from .serializers import EventViewSetSerializer
from go_green.users.models import User
from go_green.image.models import Image


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    serializer_class = EventViewSetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('creator', 'collaborators',
                     'is_cleaned', 'pollution_level')

    def get_queryset(self):
        return self.model.objects.all()

    @list_route(methods=['post'])
    def location(self, request):
        print request.data
        data = request.data
        lat = data.get('lat')
        lon = data.get('lon')
        geolocator = Nominatim()
        geo_location = geolocator.reverse('%s, %s' % (lat, lon))
        if geo_location.address:
            address = geo_location.raw['address']
            return Response(status=200, data={
                'city': address.get('city'),
                'country': address.get('country'),
                'house_number': address.get('house_number'),
                'neighbourhood': address.get('neighbourhood'),
                'road': address.get('road'),
                'state': address.get('state'),
                'suburb': address.get('suburb'),
                }
            )
        return Response(status=400)


    @list_route(methods=['post'])
    def add(self, request, format=None):
        data = request.data
        secret_token = data.get('secret_token')
        token = get_object_or_404(Token, key=secret_token)
        if secret_token:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                event = serializer.save(creator=token.user)
                return Response(status=202, data={'event_id': event.id})
            else:
                return Response(status=400, data=serializer.errors)
        return Response(status=400)

    @detail_route(methods=['post'])
    def add_collaborators(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        token = get_object_or_404(Token, key=secret_token)
        if secret_token:
            event = get_object_or_404(Event, pk=pk)
            event.collaborators.add(token.user)
            return Response(status=200)
        return Response(status=400)

    @detail_route(methods=['post'])
    def add_image_before(self, request, pk):
        data = request.data
        file = data.get('image')
        secret_token = data.get('secret_token')
        token = get_object_or_404(Token, key=secret_token)
        if secret_token:
            event = get_object_or_404(Event, pk=pk)
            image = Image.objects.create(name=file.name, image=file)
            event.image_before.add(image)
            return Response(status=200)
        return Response(status=400)

    @detail_route(methods=['post'])
    def add_image_after(self, request, pk):
        data = request.data
        file = data.get('image')
        secret_token = data.get('secret_token')
        token = get_object_or_404(Token, key=secret_token)
        if secret_token:
            event = get_object_or_404(Event, pk=pk)
            image = Image.objects.create(name=file.name, image=file)
            event.image_before.add(image)
            return Response(status=200)
        return Response(status=400)

    @detail_route(methods=['post'])
    def update(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        token = get_object_or_404(Token, key=secret_token)
        if secret_token:
            data = request.data
            qs = self.get_queryset()
            event = qs.filter(pk=pk)
            if event.exists() and event[0].creator == token.user:
                event.update(**data)
                return Response(status=204)
        return Response(status=400)
