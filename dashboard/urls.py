from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("category", views.dashboard_category, name="dashboard_category"),
    path("staff", views.dashboard_staff, name="dashboard_staff"),
    path("subcategory", views.dashboard_subcategory, name="dashboard_subcategory"),
    path("tutorialseries",views.dashboard_tutorialseries, name="dashboard_tutorialseries"),
    path("tutorialvideos", views.dashboard_tutorialvideos, name="dashboard_tutorialvideos"),
    path("addcategory", views.addcategory, name="addcategory"),
    path("addsubcategory", views.addsubcategory, name="addsubcategory"),
    path("addtutorialseries", views.addtutorialseries, name="addtutorialseries"),
    path("addtutorialvideos", views.addtutorialvideos, name="addtutorialvideos"),
]