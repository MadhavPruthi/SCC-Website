from django.urls import path

from response import views

app_name = "response"
urlpatterns = [
    path('submit_response/', views.submit_response, name="submit"),
]
