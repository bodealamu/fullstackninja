from django.shortcuts import render, redirect, get_object_or_404
from catalogue.forms import TutorialForm, TutorialVideoForm, CategoryForm, SubCategoryForm
from django.template.defaultfilters import slugify
from django.contrib import messages
from catalogue.models import Category, SubCategory, Tutorial, TutorialVideo

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


def addcategory(request):
    if request.method == "POST":
        print(request.user)

        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            title = form.cleaned_data["title"]
            slug_title = slugify(title)
            logged_in_user = request.user
            submission.author = logged_in_user
            submission.slug = slug_title
            form.save(commit=True)
            message = "Category has been successfully added."
            messages.success(request=request, message=message)

            return redirect(to= "dashboard")

    else:
        form = CategoryForm()

    context = {
        "form":form,
    }

    return render(request=request, context=context, template_name="dashboard/dashboard_addcategory.html")


def addsubcategory(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            title = form.cleaned_data["title"]
            slugged_title = slugify(title)
            logged_in_user = request.user

            submission.author = logged_in_user
            submission.slug  = slugged_title
            form.save(commit=True)
            message = "Subcategory successfully added"
            messages.success(request=request, message=message)
            return redirect(to="dashboard")

    else:
        form = SubCategoryForm()

    context = {
        "form":form,
    }

    return render(request=request, template_name="dashboard/dashboard_addsubcategory.html", context = context)


def addtutorialseries(request):
    if request.method == "POST":
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            title = form.cleaned_data["title"]
            slugged_title = slugify(title)

            submission.author = request.user
            submission.tutorial_series_slug = slugged_title
            form.save(commit=True)
            message = "Tutorial series has been successfully added."
            messages.success(request=request, message=message)
            return redirect(to="dashboard")

    else:
        form = TutorialForm()

    context = {
        "form":form
    }

    return render(request=request, context=context, template_name="dashboard/dashboard_addtutorialseries.html")


def addtutorialvideos(request):
    if request.method == "POST":
        form = TutorialVideoForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            title = form.cleaned_data["video_title"]
            slugged_title = slugify(title)
            submission.author = request.user
            submission.tutorial_video_slug = slugged_title
            form.save(commit=True)
            message = "Tutorial video added successfully."
            messages.success(request=request, message=message)
            return redirect(to="dashboard")
    else:
        form = TutorialVideoForm()

    context = {
        "form":form,
    }

    return render(request=request, context=context, template_name="dashboard/dashboard_addtutorialvideos.html")


def view_categorylist(request):
    categories = Category.objects.all()

    context = {
        "categories":categories,
    }

    return render(request=request, context=context, template_name="dashboard/categorylist.html")


def view_subcategorylist(request):
    subcategories = SubCategory.objects.all()

    context = {
        "subcategories": subcategories,
    }

    return render(request=request, context=context, template_name="dashboard/subcategorylist.html")


def view_tutorialserieslist(request):
    tutorialseries = Tutorial.objects.all()

    context = {
        "tutorialseries": tutorialseries,
    }

    return render(request=request, context=context, template_name="dashboard/tutorialserieslist.html")


def view_tutorialvideoslist(request):
    tutorialvideos = TutorialVideo.objects.all()

    context = {
        "tutorialvideos": tutorialvideos,
    }

    return render(request=request, context=context, template_name="dashboard/tutorialvideolist.html")


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.warning(request=request, message="Category has been deleted")
    return redirect(to="dashboard")


def delete_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    messages.warning(request=request, message="Subcategory has been deleted.")
    return redirect(to="dashboard")


def delete_tutorial(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    tutorial.delete()
    messages.warning(request=request, message="Tutorial series has been deleted.")
    return redirect(to="dashboard")


def delete_tutorial_video(request, pk):
    video = get_object_or_404(TutorialVideo, pk=pk)
    video.delete()
    messages.warning(request=request, message="Tutorial video has been deleted.")
    return redirect(to="dashboard")


def update_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request=request, message="Congratulations! Category has been updated.")

    return redirect(to="dashboard")


def update_subcategory(request,pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    form = SubCategoryForm(request.POST or None, request.FILES or None, instance=subcategory)

    if form.is_valid():
        form.save()
        messages.success(request=request, message="Congratulations! Subcategory has been updated.")

    return redirect(to="dashboard")


def update_tutorial(request,pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    form = TutorialForm(request.POST or None, request.FILES or None, instance=tutorial)

    if form.is_valid():
        form.save()
        messages.success(request=request, message="Congratulations! Tutorial has been updated.")

    return redirect(to="dashboard")


def update_tutorialvideo(request,pk):
    video = get_object_or_404(TutorialVideo, pk=pk)
    form = TutorialVideoForm(request.POST or None, request.FILES or None, instance=video)

    if form.is_valid():
        form.save()
        messages.success(request=request, message="Congratulations! Category has been updated.")

    return redirect(to="dashboard")

