# Generated by Django 3.0.8 on 2020-08-17 18:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0019_auto_20200817_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='managers',
            field=models.ManyToManyField(blank=True, related_name='manager_teams', to=settings.AUTH_USER_MODEL),
        ),
    ]
