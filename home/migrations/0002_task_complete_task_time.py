# Generated by Django 4.2 on 2023-04-28 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]
