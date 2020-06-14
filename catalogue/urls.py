from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalogue import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug_category>/", views.subcategories_list, name="subcategoriesview")

]