# Generated by Django 2.0.2 on 2018-04-11 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20180411_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='beer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batches', related_query_name='batch', to='inventory.Beer'),
        ),
        migrations.AlterField(
            model_name='fill',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fills', related_query_name='fill', to='inventory.Batch'),
        ),
        migrations.AlterField(
            model_name='fill',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fills', related_query_name='fill', to='accounting.Customer'),
        ),
        migrations.AlterField(
            model_name='fill',
            name='keg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fills', related_query_name='fill', to='inventory.Keg'),
        ),
    ]
