# Generated by Django 3.2.9 on 2021-12-20 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_alter_reservation_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 17, 13, 56, 98480)),
        ),
    ]