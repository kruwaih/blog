# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170717_1754'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SecondPost',
        ),
    ]
