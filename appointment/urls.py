from django.urls import path

from appointment import views

app_name = "appointment"

urlpatterns = [
    path('submit/', views.make_appointment, name="submit"),
]
