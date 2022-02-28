from django.shortcuts import render

# Create your views here.
from .models import News
import datetime
from users_profile.models import User


def news_list_view(request):
    #### FOR IP ADRESS ####
    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED_FOR')
        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    user = User(user=ip, visit_time=datetime.datetime.now())
    result = User.objects.all().filter(user=ip,
                                       visit_time__year=user.visit_time.year,
                                       visit_time__month=user.visit_time.month,
                                       visit_time__day=user.visit_time.day)

    if len(result) == 1:
        print("user exist")
    elif len(result) > 1:
        print("user exist more....")
    else:
        user.save()
        print("User is unique")

    news = News.objects.all().order_by('create_time')

    context = {
        "news": news,
    }
    return render(request, "home.html", context)
