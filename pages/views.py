from django.shortcuts import render


# Create your views here.
def gallery_view(request, *args, **kwargs):
    return render(request, "gallery.html", {})


def about_us_view(request, *args, **kwargs):
    return render(request, "about.html", {})

