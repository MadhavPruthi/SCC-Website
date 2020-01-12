from django.urls import path

from assessment import views

app_name = "assessment"
urlpatterns = [
    path('', views.assessment_page, name="assessment_page"),
    path('check_assessment/', views.check_assessment_view, name="check_assessment"),
    path('show_particular_assessment/', views.show_particular_assessment, name="show_particular_assessment"),
]
