# Generated by Django 3.2.6 on 2021-09-29 20:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210925_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 20, 16, 17, 931704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 20, 16, 17, 932410, tzinfo=utc)),
        ),
    ]