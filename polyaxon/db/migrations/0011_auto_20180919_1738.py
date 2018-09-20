# Generated by Django 2.0.8 on 2018-09-19 17:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20180916_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentchartview',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='experimentgroupchartview',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]