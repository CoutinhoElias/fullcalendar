# Generated by Django 2.0.4 on 2018-04-24 19:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20180411_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
