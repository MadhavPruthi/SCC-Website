from datetime import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import redirect

from appointment.models import Appointment


def make_appointment(request):
    if request.method == 'POST':
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
        return redirect('home')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
