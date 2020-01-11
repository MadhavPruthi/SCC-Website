from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from assessment import urls as assessment_urls
from response import urls as response_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('assessment/', include(assessment_urls)),
    path('response/', include(response_urls)),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
    path('privacy_calmminds/', TemplateView.as_view(template_name="privacyPolicy.html"))
]
