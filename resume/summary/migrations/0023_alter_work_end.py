# Generated by Django 3.2.12 on 2022-03-11 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0022_alter_work_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 11, 12, 32, 10, 287088), null=True),
        ),
    ]
