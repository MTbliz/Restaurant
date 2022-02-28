from django.contrib import admin
from .models import Meal, MealOfTheDay, SetOfTheDay, MealsSetofthedayMealsoftheday


# Register your models here.


class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category']
    list_filter = ['category']


class InlineMealOfTheDay(admin.TabularInline):
    model = MealsSetofthedayMealsoftheday
    verbose_name = "List of Meals of the day"
    readonly_fields = ['meal_title', 'meal_price', 'meal_category']

    def meal_title(self, instance):
        return instance.mealOfDay.title

    meal_title.short_description = 'Title'

    def meal_price(self, instance):
        return instance.mealOfDay.price

    meal_price.short_description = 'Price'

    def meal_category(self, instance):
        return instance.mealOfDay.category

    meal_category.short_description = 'Category'


class MealOfTheDayAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'img']
    list_filter = ['category']


class SetOfTheDayAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'display_meals']
    inlines = [InlineMealOfTheDay]
    list_filter = ['title']
    exclude = ['mealsOfTheDay']


admin.site.register(Meal, MealAdmin)
admin.site.register(MealOfTheDay, MealOfTheDayAdmin)
admin.site.register(SetOfTheDay, SetOfTheDayAdmin)
