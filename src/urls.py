from django.contrib import admin
from django.contrib.flatpages import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

from appointment import urls as appointment_urls
from assessment import urls as assessment_urls
from authentication import urls as auth_urls
from response import urls as response_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('', TemplateView.as_view(template_name="public/index.html"), name="home"),
    path('auth/', include(auth_urls)),
    path('assessment/', include(assessment_urls)),
    path('response/', include(response_urls)),
    path('appointment/', include(appointment_urls)),
    path('about/', TemplateView.as_view(template_name="public/about.html")),
    path('contact/', TemplateView.as_view(template_name="public/contact.html")),
    path('privacy_calmminds/', TemplateView.as_view(template_name="public/privacyPolicy.html")),
]
