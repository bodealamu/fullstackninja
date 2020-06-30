from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path("login/", authentication_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    path("password_change/",
         authentication_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"),
         name="password_change"),
    path("password_change/done/",
         authentication_views.PasswordChangeDoneView.as_view(template_name="accounts/passwordchangedone.html"),
         name="password_change_done"),
    path("password_reset/", authentication_views.PasswordResetView.as_view(template_name="accounts/passwordreset.html"),
         name="password_reset"),



]