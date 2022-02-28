"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from pages.views import gallery_view, about_us_view
from meals.views import meal_list_view, set_of_the_day_list_view
from reservations.views import reservation_create_view
from restaurant_statistics.views import restaurant_statistics_view
from news.views import news_list_view

urlpatterns = [
                  path('', news_list_view, name='home'),
                  path('meal_of_the_day/', set_of_the_day_list_view, name='meal_of_the_day'),
                  path('menu/', meal_list_view, name='menu'),
                  path('reservations/', reservation_create_view, name='reservations'),
                  path('gallery/', gallery_view, name='gallery'),
                  path('about/', about_us_view, name='about'),
                  path('statistics/', restaurant_statistics_view, name='res-statistics'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
