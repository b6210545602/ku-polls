# Generated by Django 3.1 on 2020-10-30 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20201030_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 16, 3, 18, 992004, tzinfo=utc), verbose_name='date ended'),
        ),
    ]