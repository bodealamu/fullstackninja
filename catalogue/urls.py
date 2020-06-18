from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalogue import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:category_slug>/", views.subcategories_list, name="subcategoriesview"),
    path("allsubcategories", views.all_subcategorylist, name="allsubcategories"),
    path("alltutorialserieslist", views.all_tutorialserieslist, name="alltutorialserieslist"),
    path("<str:category_slug>/<str:slug_subcategory>/", views.tutorial_series_list, name="hometutorialseries"),
]