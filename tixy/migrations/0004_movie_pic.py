# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tixy', '0003_auto_20171004_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pic',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]