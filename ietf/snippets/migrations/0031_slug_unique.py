# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-19 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0030_populate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondarytopic',
            name='slug',
            field=models.CharField(max_length=511, unique=True),
        ),
    ]