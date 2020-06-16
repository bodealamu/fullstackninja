from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request=request, context=None, template_name="dashboard/dashboard.html")
