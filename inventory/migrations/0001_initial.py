# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-02 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import inventory.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keg',
            fields=[
                ('created', inventory.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', inventory.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'keg',
                'verbose_name_plural': 'kegs',
                'ordering': ('created',),
            },
        ),
    ]
