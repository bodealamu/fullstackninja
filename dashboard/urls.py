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
    path("categorylist", views.view_categorylist, name="categorylist"),
    path("subcategorylist", views.view_subcategorylist, name="subcategorylist"),
    path("tutorialserieslist", views.view_tutorialserieslist, name="tutorialserieslist"),
    path("tutorialvideoslist", views.view_tutorialvideoslist, name="tutorialvideoslist"),
    path("deletecategory/<int:pk>",views.delete_category, name="deletecategory"),
    path("deletesubcategory/<int:pk>",views.delete_subcategory, name="deletesubcategory"),
    path("deletetutorial/<int:pk>",views.delete_tutorial, name="deletetutorial"),
    path("deletetutorialvideo/<int:pk>",views.delete_tutorial_video, name="deletetutorialvideo"),
    path("updatecategory/<int:pk>", views.update_category, name="updatecategory"),
    path("updatesubcategory/<int:pk>", views.update_subcategory, name="updatesubcategory"),
    path("updatetutorial/<int:pk>", views.update_tutorial, name="updatetutorial"),
    path("updatetutorialvideo/<int:pk>", views.update_tutorialvideo, name="updatetutorialvideo"),
]