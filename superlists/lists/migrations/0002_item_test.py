# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-28 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='test',
            field=models.TextField(default=''),
        ),
    ]
