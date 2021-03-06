from django.shortcuts import render, redirect
from catalogue.models import Category, SubCategory, Tutorial, TutorialVideo, Contact, Courses
from django.shortcuts import get_object_or_404
from catalogue.forms import ContactForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib import messages


# Create your views here.
def course_list(request):
    """View function for courses"""
    course_list = Courses.objects.all()

    context = {
        "courses":course_list
    }

    return render(request=request, context=context, template_name="catalogue/courses.html")


def contactpage(request):
    """View function for handling contact page messages."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your Contact message has been sent."
            messages.success(request=request, message=message)

            return redirect(to="home")


    else:
        form = ContactForm()

    context = {
        "form":form,
    }

    return render(request=request, context=context, template_name="catalogue/contact.html")


def home(request):
    """
    View function for the home page, it shows all the categories available on the site
    :param request:
    :return:
    """
    UserModel = get_user_model()
    print(UserModel)
    categories = Category.objects.all()
    all_videos = TutorialVideo.objects.all()

    number_tutorial_videos = len(all_videos)


    context={
        "categories":categories,
        "number_tutorial_videos":number_tutorial_videos,
    }

    return render(request=request, template_name="catalogue/home.html", context=context)


def subcategories_list(request, category_slug):
    """
    A list view for all the subcategories under a category
    :param request:
    :param slug_subcategory: str, url slug for the chosen subcategory
    :return:
    """
    category = get_object_or_404(Category,slug=category_slug)
    # find all sub categories whose category slug is given
    subcategories = SubCategory.objects.filter(classification=category)

    context = {
        "subcategories":subcategories,
        "singlecategory":category
    }

    return render(request=request, template_name="catalogue/subcategorieslist.html", context=context)


def tutorial_videos_list(request, category_slug, slug_subcategory, tutorial_series_slug):
    """
    View function which lists out all the tutorial videos which belong to a tutorial series, subcategory and category
    :param request:
    :param category_slug:
    :param slug_subcategory:
    :param tutorial_series_slug:
    :return:
    """
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=slug_subcategory)
    tutorial_series = get_object_or_404(Tutorial, tutorial_series_slug=tutorial_series_slug)
    print(tutorial_series_slug)
    print("jjhhgghjgg")
    print(tutorial_series)
    tutorial_videos = TutorialVideo.objects.filter(tutorial_category=tutorial_series)
    print(tutorial_videos)

    # for tut in tutorial_videos:
    #     print(tut.tutorial_video_slug)

    context={
        "category":category,
        "subcategory":subcategory,
        "tutorial_series":tutorial_series,
        "tutorial_videos":tutorial_videos,
    }

    return render(request=request, context=context, template_name="catalogue/tutorialvideos.html")


def tutorial_videos_details(request, category_slug, slug_subcategory, tutorial_series_slug, video_slug):
    """
    View function which lists out all the tutorial videos which belong to a tutorial series, subcategory and category
    :param request:
    :param category_slug:
    :param slug_subcategory:
    :param tutorial_series_slug:
    :return:
    """
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=slug_subcategory)
    tutorial_series = get_object_or_404(Tutorial, tutorial_series_slug=tutorial_series_slug)

    tutorial_videos = TutorialVideo.objects.filter(tutorial_category=tutorial_series)
    print(tutorial_videos)

    video = get_object_or_404(TutorialVideo, tutorial_video_slug=video_slug)
    print(video)
    all_subcategories = SubCategory.objects.filter(classification=category)



    context={
        "category":category,
        "subcategory":subcategory,
        "tutorial_series":tutorial_series,
        "tutorial_videos":tutorial_videos,
        "videofile":video,
        "all_subcategories": all_subcategories,
    }

    return render(request=request, context=context, template_name="catalogue/videodetail.html")


def tutorial_series_list(request, category_slug,  slug_subcategory):
    """
    :param request:
    :param slug_subcategory: slug for the subcategory which has the tutorial series
    :return:
    """
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=slug_subcategory)

    tutorial_series = Tutorial.objects.filter(tutorial_category=subcategory)

    context = {
        "subcategory":subcategory,
        "tutorialseries":tutorial_series,
        "category":category,
    }

    return render(request=request, template_name="catalogue/tutorialseries.html",context=context)


def all_subcategorylist(request):
    """View function for viewing all tutorial subcategory objects"""
    subcategories = SubCategory.objects.all()

    context = {
        "subcategories": subcategories,
    }

    return render(request=request, context=context, template_name="catalogue/allsubcategorylist.html")


def all_tutorialserieslist(request):
    """View function for viewing all tutorial series objects"""
    tutorialseries = Tutorial.objects.all()

    context = {
        "tutorialseries": tutorialseries,
    }

    return render(request=request, context=context, template_name="catalogue/alltutorialserieslist.html")







