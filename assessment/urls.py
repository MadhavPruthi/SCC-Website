from django.urls import path

from assessment import views

app_name = "assessment"
urlpatterns = [
    path('', views.assessment_page, name="assessment_page"),
]
