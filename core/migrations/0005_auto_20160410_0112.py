# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160410_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='finished',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
