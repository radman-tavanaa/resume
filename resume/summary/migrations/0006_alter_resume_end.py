# Generated by Django 3.2.6 on 2022-02-13 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0005_alter_resume_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 13, 21, 44, 55, 154471), null=True),
        ),
    ]
