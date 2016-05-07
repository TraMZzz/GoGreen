# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json

from django.shortcuts import get_object_or_404

from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import (
    exceptions, filters, mixins, pagination,
    permissions, serializers, status, viewsets)
from rest_framework.authtoken.models import Token


from .models import User
from .serializers import UserViewSetSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserViewSetSerializer

    def get_queryset(self):
        return self.model.objects.all()

    @list_route(methods=['post'])
    def add(self, request, format=None):
        data = request.data
        uid = data.get('uid')
        if uid:
            token = Token.objects.filter(user__uid=uid)
            if token.exists():
                return Response(status=202, data={'token': token[0].key, 'id': token[0].user.id})
            else:
                serializer = self.serializer_class(data=data)
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.get(uid=uid)
                    token = Token.objects.create(user=User.objects.get(uid=uid))
                    return Response(status=202, data={'token': token.key, 'id': user.id})
                else:
                   return Response(status=400, data=serializer.errors)
        return Response(status=400)

    @detail_route(methods=['post'])
    def update(self, request, pk):
        data = request.data
        secret_token = data.get('secret_token')
        if secret_token:
            qs = self.get_queryset()
            user = qs.filter(pk=pk)
            if user.exists():
                user.update(**data)
                return Response(status=204)
        return Response(status=400)
