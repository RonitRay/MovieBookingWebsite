# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tixy', '0002_auto_20171004_1943'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]