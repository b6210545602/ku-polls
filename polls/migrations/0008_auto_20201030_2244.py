# Generated by Django 3.1 on 2020-10-30 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20201030_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 15, 44, 48, 515349, tzinfo=utc), verbose_name='date ended'),
        ),
    ]
