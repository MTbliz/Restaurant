# Generated by Django 4.0 on 2022-02-20 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_mealoftheday'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetOfTheDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='MealsSetofthedayMealsoftheday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealOfDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.mealoftheday')),
                ('setOfDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.setoftheday')),
            ],
        ),
    ]
