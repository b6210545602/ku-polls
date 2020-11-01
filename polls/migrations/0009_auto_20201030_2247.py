# Generated by Django 3.1 on 2020-10-30 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20201030_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='last_vote',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 15, 47, 34, 731089, tzinfo=utc), verbose_name='date ended'),
        ),
    ]