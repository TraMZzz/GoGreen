# -*- coding: utf-8 -*-

from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

from go_green.badge.serializers import BadgeViewSetSerializer


class UserViewSetSerializer(serializers.ModelSerializer):
    badges = BadgeViewSetSerializer(many=True, read_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = (u'id', u'username', u'email', u'first_name',
                  u'last_name', u'clean_count',
                  u'status', u'is_volunteer', u'volunteer_group_name',
                  u'show_contact', u'contact_email', u'contact_phone',
                  u'contact_url', u'badges', u'uid', u'extra_data',
                  u'token', u'expires_at')

    def validate_contact_email(self, attrs):
        contact_email = attrs
        if contact_email:
                emailset = Q(contact_email__icontains=contact_email)
                emailres = User.objects.filter(emailset)
                if emailres:
                        msg = _('The email address is already taken')
                        raise serializers.ValidationError(msg)
                else:
                    return attrs
