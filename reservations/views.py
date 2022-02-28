from django.shortcuts import render
import logging
from .forms import ReservationForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create a logger for this file
# logger = logging.getLogger(__name__)


# Create your views here.
def send_email_custom(request):
    first_name = request.POST.get('name', '')
    last_name = request.POST.get('last_name', '')
    subject = f"{last_name}_{first_name}_reservation"
    message = request.POST.get('description', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            print(subject)
            # send_mail(subject, message, from_email, ['test@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('reservations.html')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def reservation_create_view(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        # form.save()
        send_email_custom(request)
        form = ReservationForm()
    context = {
        'form': form,
        'first_name': request.POST.get('name', '')
    }
    return render(request, "reservations.html", context)
