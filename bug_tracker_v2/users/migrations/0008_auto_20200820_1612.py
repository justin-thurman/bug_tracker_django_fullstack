# Generated by Django 3.0.8 on 2020-08-20 20:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200820_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='notification_settings',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]
