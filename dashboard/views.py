from django.shortcuts import render, redirect, get_object_or_404
from catalogue.forms import TutorialForm, TutorialVideoForm, CategoryForm, SubCategoryForm
from django.template.defaultfilters import slugify
from django.contrib import messages
from catalogue.models import Category, SubCategory, Tutorial, TutorialVideo, Contact
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


@staff_member_required(login_url="accounts/login.html")
def dashboard(request):
    return render(request=request, context=None, template_name="dashboard/dashboard.html")


@staff_member_required(login_url="accounts/login.html")
def dashboard_category(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_category.html")


@staff_member_required(login_url="accounts/login.html")
def dashboard_staff(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_staff.html")


@staff_member_required(login_url="accounts/login.html")
def dashboard_subcategory(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_subcategory.html")


@staff_member_required(login_url="accounts/login.html")
def dashboard_tutorialseries(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_Tutorialseries.html")


@staff_member_required(login_url="accounts/login.html")
def dashboard_tutorialvideos(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_Tutorialvideos.html")


@staff_member_required(login_url="accounts/login.html")
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


@staff_member_required(login_url="accounts/login.html")
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


@staff_member_required(login_url="accounts/login.html")
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


@staff_member_required(login_url="accounts/login.html")
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


@staff_member_required(login_url="accounts/login.html")
def view_categorylist(request):
    categories = Category.objects.all()

    context = {
        "categories":categories,
    }

    return render(request=request, context=context, template_name="dashboard/categorylist.html")


@staff_member_required(login_url="accounts/login.html")
def view_subcategorylist(request):
    subcategories = SubCategory.objects.all()

    context = {
        "subcategories": subcategories,
    }

    return render(request=request, context=context, template_name="dashboard/subcategorylist.html")


@staff_member_required(login_url="accounts/login.html")
def view_tutorialserieslist(request):
    tutorialseries = Tutorial.objects.all()

    context = {
        "tutorialseries": tutorialseries,
    }

    return render(request=request, context=context, template_name="dashboard/tutorialserieslist.html")


@staff_member_required(login_url="accounts/login.html")
def view_tutorialvideoslist(request):
    tutorialvideos = TutorialVideo.objects.all()

    context = {
        "tutorialvideos": tutorialvideos,
    }

    return render(request=request, context=context, template_name="dashboard/tutorialvideolist.html")


@staff_member_required(login_url="accounts/login.html")
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.warning(request=request, message="Category has been deleted")
    return redirect(to="dashboard")


@staff_member_required(login_url="accounts/login.html")
def delete_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    messages.warning(request=request, message="Subcategory has been deleted.")
    return redirect(to="dashboard")


@staff_member_required(login_url="accounts/login.html")
def delete_tutorial(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    tutorial.delete()
    messages.warning(request=request, message="Tutorial series has been deleted.")
    return redirect(to="dashboard")


@staff_member_required(login_url="accounts/login.html")
def delete_tutorial_video(request, pk):
    video = get_object_or_404(TutorialVideo, pk=pk)
    video.delete()
    messages.warning(request=request, message="Tutorial video has been deleted.")
    return redirect(to="dashboard")


@staff_member_required(login_url="accounts/login.html")
def update_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request=request, message="Congratulations! Category has been updated.")
        return redirect(to="dashboard")

    context={
        "form":form,
    }

    return render(request=request, context=context, template_name="dashboard/dashboard_addcategory.html")


@staff_member_required(login_url="accounts/login.html")
def update_subcategory(request,pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    form = SubCategoryForm(request.POST or None, request.FILES or None, instance=subcategory)

    if form.is_valid():
        form.save()
        messages.success(request=request, message="Congratulations! Subcategory has been updated.")
        return redirect(to="dashboard")
    context={
        "form":form,
    }

    return render(request=request, template_name="dashboard/dashboard_addsubcategory.html", context=context)


@staff_member_required(login_url="accounts/login.html")
def update_tutorial(request,pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    form = TutorialForm(request.POST or None, request.FILES or None, instance=tutorial)

    if form.is_valid():
        form.save()
        messages.success(request=request, message="Congratulations! Tutorial has been updated.")
        return redirect(to="dashboard")

    context={
        "form":form,
    }

    return render(request=request, context=context, template_name="dashboard/dashboard_addtutorialseries.html")


@staff_member_required(login_url="accounts/login.html")
def update_tutorialvideo(request, pk):
    video = get_object_or_404(TutorialVideo, pk=pk)
    form = TutorialVideoForm(request.POST or None, request.FILES or None, instance=video)

    if form.is_valid():
        form.save()
        messages.success(request=request, message="Congratulations! Tutorial video has been updated.")
        return redirect(to="dashboard")

    context={
        "form":form,
    }

    return render(request=request, context=context, template_name="dashboard/dashboard_addtutorialvideos.html")


@staff_member_required(login_url="accounts/login.html")
def dashboard_messages(request):
    return render(request=request, context=None, template_name="dashboard/dashboard_messages.html")


@staff_member_required(login_url="accounts/login.html")
def view_read_messages(request):
    read_messages = Contact.objects.filter(message_read=True)

    context = {
        "read_messages": read_messages,
    }

    return render(context=context, request=request, template_name="dashboard/read_messages.html")


@staff_member_required(login_url="accounts/login.html")
def view_unread_messages(request):
    unread_messages = Contact.objects.filter(message_read=False)

    context = {
        "unread_messages":unread_messages,
    }

    return render(context=context, request=request, template_name="dashboard/unread_messages.html")


@staff_member_required(login_url="accounts/login.html")
def delete_read_messages(request, pk):
    read_message = get_object_or_404(Contact, pk=pk)
    print(read_message)
    read_message.delete()

    messages.warning(request=request, message="Message has been deleted.")

    return redirect(to="dashboard")


@staff_member_required(login_url="accounts/login.html")
def mark_as_read(request, pk):
    unread_message = get_object_or_404(Contact, pk=pk)
    unread_message.message_read = True
    unread_message.save()
    messages.success(request=request, message="Message has been read.")

    return redirect(to="viewreadmessages")

