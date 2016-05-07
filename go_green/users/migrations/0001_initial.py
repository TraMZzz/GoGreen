# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 17:22
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import go_green.users.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('badge', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('clean_count', models.PositiveIntegerField(default=0, verbose_name='Clean rating')),
                ('status', models.CharField(blank=True, max_length=55, verbose_name='Status')),
                ('is_volunteer', models.BooleanField(default=False, verbose_name='Volunteer ?')),
                ('volunteer_group_name', models.CharField(blank=True, max_length=100, verbose_name='Volunteer Group Name')),
                ('show_contact', models.BooleanField(default=True, verbose_name='Show Contact ?')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Contact email')),
                ('contact_phone', models.CharField(blank=True, max_length=100, verbose_name='Contact phone')),
                ('contact_url', models.URLField(blank=True, max_length=100, verbose_name='Contact url')),
                ('uid', models.CharField(max_length=200, unique=True, verbose_name='uid')),
                ('extra_data', go_green.users.fields.JSONField(default=dict, verbose_name='extra data')),
                ('token', models.TextField(blank=True, verbose_name='token provider')),
                ('expires_at', models.DateTimeField(blank=True, null=True, verbose_name='expires at')),
                ('badges', models.ManyToManyField(blank=True, db_table='users_badges', related_name='badges', to='badge.Badge')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('uid', 'token')]),
        ),
    ]
