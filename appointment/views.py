from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

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


@login_required()
def view_appointments(request):
    if request.method == 'GET':
        data = Appointment.objects.all()
        context = {"data": data}
        return render(request, 'appointmentRequests.html', context);

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
