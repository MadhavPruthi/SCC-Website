from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import FormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('assessment/', TemplateView.as_view(template_name="dass21.html")),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('blog-home', TemplateView.as_view(template_name="blog-home.html")),
    path('blog-details', TemplateView.as_view(template_name="blog-details.html")),
    path('contact', TemplateView.as_view(template_name="contact.html")),
]
