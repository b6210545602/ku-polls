# Generated by Django 3.1 on 2020-10-30 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200918_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 13, 27, 1, 405116, tzinfo=utc), verbose_name='date ended'),
        ),
    ]