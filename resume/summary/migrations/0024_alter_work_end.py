# Generated by Django 3.2.12 on 2022-03-11 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0023_alter_work_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 11, 12, 40, 14, 107836), null=True),
        ),
    ]
