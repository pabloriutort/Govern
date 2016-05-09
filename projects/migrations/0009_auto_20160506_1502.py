# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_evaluacio_data_modificacio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluacio',
            old_name='data_modificacio',
            new_name='modificat',
        ),
        migrations.AddField(
            model_name='evaluacio',
            name='creat',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 6, 15, 2, 1, 609478, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projecte',
            name='creat',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 6, 15, 2, 6, 171979, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projecte',
            name='modificat',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 5, 6, 15, 2, 18, 204682, tzinfo=utc)),
            preserve_default=False,
        ),
    ]