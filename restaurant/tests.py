from django.test import SimpleTestCase
from django.urls import reverse, resolve
from meals.views import set_of_the_day_list_view, meal_list_view
from reservations.views import reservation_create_view
from pages.views import gallery_view, about_us_view
from restaurant_statistics.views import restaurant_statistics_view
from news.views import news_list_view


class TestUrls(SimpleTestCase):

    def test_restaurant_statistics_view_url_is_resolver(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, news_list_view)

    def test_set_of_the_day_list_view_url_is_resolver(self):
        url = reverse('meal_of_the_day')
        self.assertEquals(resolve(url).func, set_of_the_day_list_view)
        
    def test_meal_list_view_url_is_resolver(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func, meal_list_view)

    def test_gallery_view_url_is_resolver(self):
        url = reverse('gallery')
        self.assertEquals(resolve(url).func, gallery_view)

    def test_reservation_create_view_url_is_resolver(self):
        url = reverse('reservations')
        self.assertEquals(resolve(url).func, reservation_create_view)

    def test_about_us_view_url_is_resolver(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about_us_view)

    def test_restaurant_statistics_view_url_is_resolver(self):
        url = reverse('res-statistics')
        self.assertEquals(resolve(url).func, restaurant_statistics_view)