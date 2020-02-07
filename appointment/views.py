from datetime import datetime
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from appointment.models import Appointment
from src import settings


def make_appointment(request):
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post(url=url, data=data)
        result = r.json()
        print(result)
        if result['success']:
            data = request.POST
            datetime_object = datetime.strptime(data['date'], '%d-%m-%Y %I:%M %p')
            appointment = Appointment(
                name=data['name'],
                message=data['message'],
                email=data['email'],
                contactNumber=data['contactNumber'],
                date=datetime_object
            )
            appointment.save()
            return render(request, 'public/appointmentSubmission.html', {})
        else:
            return HttpResponseNotFound('<h1>Invalid ReCAPTCHA</h1>')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


@login_required()
def view_appointments(request):
    if request.method == 'GET':
        data = Appointment.objects.all()
        context = {"data": data}
        return render(request, 'admin/appointmentRequests.html', context);

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
