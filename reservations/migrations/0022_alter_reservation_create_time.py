# Generated by Django 4.0 on 2022-02-20 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0021_alter_reservation_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 18, 54, 0, 386841)),
        ),
    ]
