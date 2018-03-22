# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-02 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keg',
            name='litres',
            field=models.IntegerField(choices=[(50, '50 Litres'), (30, '30 Litres'), (20, '20 Litres')], default=50, max_length=100),
        ),
    ]