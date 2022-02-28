from django.db import models
from django.dispatch import receiver
import os


# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.CharField(max_length=50)


class MealOfTheDay(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images', height_field=None, width_field=None)

    def __str__(self):
        return f'{self.title} | {self.price} zł | {self.category}'


class SetOfTheDay(models.Model):
    title = models.CharField(max_length=120)
    mealsOfTheDay = models.ManyToManyField(MealOfTheDay, through='MealsSetofthedayMealsoftheday')
    active = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.active:
            SetOfTheDay.objects.all().filter(active=True).update(active=False)
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        if self.active:
            SetOfTheDay.objects.all().filter(active=True).update(active=False)
        super().update(*args, **kwargs)

    def display_meals(self):
        """Create a string for the MealOfTheDay. This is required to display MealOfTheDay in Admin."""
        return ', '.join(meal.title for meal in self.mealsOfTheDay.all()[:3])

    display_meals.short_description = 'Meals Of the Day'


class MealsSetofthedayMealsoftheday(models.Model):
    mealOfDay = models.ForeignKey(MealOfTheDay, on_delete=models.CASCADE)
    setOfDay = models.ForeignKey(SetOfTheDay, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


@receiver(models.signals.post_delete, sender=MealOfTheDay)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=MealOfTheDay)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False
