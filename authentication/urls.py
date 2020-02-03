from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "authentication"

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='admin/login.html', redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
