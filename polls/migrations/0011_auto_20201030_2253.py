# Generated by Django 3.1 on 2020-10-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20201030_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='date ended'),
        ),
    ]