from django.shortcuts import render
from catalogue.models import Category, SubCategory, Tutorial, TutorialVideo

# Create your views here.


def home(request):
    """
    View function for the home page, it shows all the categories available on the site
    :param request:
    :return:
    """
    categories = Category.objects.all()

    context={
        "categories":categories,
    }

    return render(request=request, template_name="catalogue/home.html", context=context)


def subcategories_list(request, slug_category):
    """
    A list view for all the subcategories
    :param request:
    :param slug_subcategory: str, url slug for the chosen subcategory
    :return:
    """
    # find all sub categories whose category slug is given
    subcategories = SubCategory.objects.filter(Category_category_slug=slug_category)

    context = {
        "subcategories":subcategories,
    }

    return render(request=request, template_name="catalogue/subcategorieslist.html", context=context)


def tutorial_series_list(request,slug_category ,slug_subcategory):
    """

    :param request:
    :param slug_subcategory: slug for the subcategory which has the tutorial series
    :return:
    """
    tutorial_series = Tutorial.objects.filter(subcategory_subcategory_slug=slug_subcategory)

    context = {
        "tutorial_series":tutorial_series,
    }

    return render(request=request, template_name="catalogue/tutorialseries.html",context=context)


def all_subcategorylist(request):
    subcategories = SubCategory.objects.all()

    context = {
        "subcategories": subcategories,
    }

    return render(request=request, context=context, template_name="catalogue/allsubcategorylist.html")


def all_tutorialserieslist(request):
    tutorialseries = Tutorial.objects.all()

    context = {
        "tutorialseries": tutorialseries,
    }

    return render(request=request, context=context, template_name="catalogue/tutorialserieslist.html")


# def view_tutorialvideoslist(request):
#     tutorialvideos = TutorialVideo.objects.all()
#
#     context = {
#         "tutorialvideos": tutorialvideos,
#     }
#
#     return render(request=request, context=context, template_name="dashboard/tutorialvideolist.html")



