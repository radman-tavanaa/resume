# Generated by Django 3.2.12 on 2022-03-02 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0016_alter_work_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 2, 15, 56, 34, 448069), null=True),
        ),
    ]
