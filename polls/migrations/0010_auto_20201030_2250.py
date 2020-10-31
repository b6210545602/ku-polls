# Generated by Django 3.1 on 2020-10-30 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20201030_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 15, 50, 9, 81248, tzinfo=utc), verbose_name='date ended'),
        ),
    ]
