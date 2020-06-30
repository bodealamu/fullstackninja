from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path("login/", authentication_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout', authentication_views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),


]