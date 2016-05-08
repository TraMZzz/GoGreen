# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404

from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import (
    exceptions, filters, mixins, pagination,
    permissions, serializers, status, viewsets)

from .models import Event
from .serializers import EventViewSetSerializer
from go_green.users.models import User


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    serializer_class = EventViewSetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('creator', 'collaborators',)

    def get_queryset(self):
        return self.model.objects.all()

    @list_route(methods=['post'])
    def add(self, request, format=None):
        data = request.data
        secret_token = data.get('secret_token')
        uid = data.get('uid')
        user = get_object_or_404(User, uid=uid)
        if secret_token:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save(creator=user)
                return Response(status=202)
            else:
                return Response(status=400, data=serializer.errors)
        return Response(status=400)

    @detail_route(methods=['post'])
    def add_collaborators(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        uid = data.get('uid')
        user = get_object_or_404(User, uid=uid)
        if secret_token:
            event = get_object_or_404(Event, pk=pk)
            event.collaborators.add(user)
            return Response(status=200)
        return Response(status=400)

    @detail_route(methods=['post'])
    def add_image_before(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        if secret_token:
            event = get_object_or_404(Event, pk=pk)
            print request.POST
            print pk
            return Response(status=200)
        return Response(status=400)

    @detail_route(methods=['post'])
    def add_image_after(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        if secret_token:
            event = get_object_or_404(Event, pk=pk)
            print request.POST
            print pk
            return Response(status=200)
        return Response(status=400)

    def update(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        if secret_token:
            data = request.data
            qs = self.get_queryset()
            event = qs.filter(pk=pk)
            if event.exists():
                event.update(**data)
                return Response(status=204)
        return Response(status=400)
