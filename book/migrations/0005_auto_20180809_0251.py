# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-09 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20180809_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='upc',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
