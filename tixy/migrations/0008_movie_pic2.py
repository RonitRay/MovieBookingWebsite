# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tixy', '0007_auto_20171012_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pic2',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
