# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_scheduling', '0002_auto_20160725_1600'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReservationModel',
            new_name='Reservation',
        ),
        migrations.RenameModel(
            old_name='RoomModel',
            new_name='Room',
        ),
    ]
