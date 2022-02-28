from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
from users_profile.models import User
from reservations.models import Reservation
from meals.models import Meal


# Create your views here.
def restaurant_statistics_view(request, *args, **kwargs):
    users_all = User.objects.all() \
        .annotate(year_month_day=TruncDay('visit_time')) \
        .values('year_month_day') \
        .annotate(total=Count('id')) \
        .order_by('year_month_day')

    users = User.objects.all() \
        .annotate(year_month=TruncMonth('visit_time')) \
        .values('year_month') \
        .annotate(total=Count('id')) \
        .order_by('year_month')

    reservations_all = Reservation.objects.all() \
        .annotate(year_month_day=TruncDay('create_time')) \
        .values('year_month_day') \
        .annotate(total=Count('id')) \
        .order_by('year_month_day')

    reservations = Reservation.objects.all() \
        .annotate(year_month=TruncMonth('create_time')) \
        .values('year_month') \
        .annotate(total=Count('id')) \
        .order_by('year_month')

    meal_categories = Meal.objects.all() \
        .values('category') \
        .annotate(total=Count('id')) \
        .order_by('category')
    return render(request, "restaurant_statistics.html", {'users': users,
                                                          'reservations': reservations,
                                                          'meal_categories': meal_categories,
                                                          'users_all': users_all,
                                                          'reservations_all': reservations_all})
