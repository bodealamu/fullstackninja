from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request=request, context=None, template_name="dashboard/dashboard.html")


def dashboard_category(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_category.html")


def dashboard_staff(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_staff.html")


def dashboard_subcategory(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_subcategory.html")


def dashboard_tutorialseries(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_Tutorialseries.html")


def dashboard_tutorialvideos(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_Tutorialvideos.html")