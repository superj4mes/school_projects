# Generated by Django 3.2.6 on 2021-09-29 20:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20210929_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 20, 57, 46, 775163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 20, 57, 46, 775762, tzinfo=utc)),
        ),
    ]
