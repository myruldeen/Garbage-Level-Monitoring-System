# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readings',
            name='dustbin_id',
        ),
    ]
