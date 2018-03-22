# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-03 06:30
from __future__ import unicode_literals

import common.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('created', common.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', common.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('qbid', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'ordering': ('created',),
            },
        ),
    ]