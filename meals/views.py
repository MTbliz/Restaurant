from django.shortcuts import render
from .models import Meal, MealOfTheDay, SetOfTheDay


# Create your views here.
def meal_list_view(request):
    meat_meals = Meal.objects.all().filter(category="MEAT").order_by('title')
    soup_meals = Meal.objects.all().filter(category="SOUP").order_by('title')
    cold_appetizers = Meal.objects.all().filter(category="COLD_APPETIZER").order_by('title')
    hot_appetizers = Meal.objects.all().filter(category="HOT_APPETIZER").order_by('title')
    sets = Meal.objects.all().filter(category="SET").order_by('title')
    salads = Meal.objects.all().filter(category="SALAD").order_by('title')
    pasta_meals = Meal.objects.all().filter(category="PASTA").order_by('title')
    fish_meals = Meal.objects.all().filter(category="FISH").order_by('title')
    desserts = Meal.objects.all().filter(category="DESSERT").order_by('title')
    additions = Meal.objects.all().filter(category="ADDITION").order_by('title')
    context = {
        "meat_meals": meat_meals,
        "soup_meals": soup_meals,
        "cold_appetizers": cold_appetizers,
        "hot_appetizers": hot_appetizers,
        "sets": sets,
        "salads": salads,
        "pasta_meals": pasta_meals,
        "fish_meals": fish_meals,
        "additions": additions,
        "desserts": desserts,
    }
    return render(request, "menu.html", context)


def set_of_the_day_list_view(request):
    # Query meals by lazy querysetevaluation
    sets_of_the_day = SetOfTheDay.objects.all().filter(active=True)
    meals_of_the_day = MealOfTheDay.objects.all().filter(setoftheday__in=sets_of_the_day)

    context = {
        "meals_of_the_day": meals_of_the_day,
    }
    return render(request, "meal_of_the_day.html", context)
