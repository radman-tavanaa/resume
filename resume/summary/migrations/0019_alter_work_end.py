# Generated by Django 3.2.12 on 2022-03-10 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0018_alter_work_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 10, 16, 23, 1, 384271), null=True),
        ),
    ]
