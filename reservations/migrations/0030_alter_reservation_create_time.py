# Generated by Django 4.0 on 2022-02-20 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0029_alter_reservation_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 19, 33, 26, 769960)),
        ),
    ]
