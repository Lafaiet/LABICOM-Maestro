# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 19:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room_scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationmodel',
            name='event_name',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='user_requester',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
