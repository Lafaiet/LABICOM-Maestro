# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 19:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_scheduling', '0006_reservation_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='start_end',
            new_name='end_time',
        ),
    ]