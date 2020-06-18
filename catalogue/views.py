from django.shortcuts import render
from catalogue.models import Category, SubCategory, Tutorial, TutorialVideo
from django.shortcuts import get_object_or_404

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
    print(subcategories)

    context = {
        "subcategories":subcategories,
    }

    return render(request=request, template_name="catalogue/subcategorieslist.html", context=context)


def tutorial_series_list(request,category_slug,  slug_subcategory):
    """
    :param request:
    :param slug_subcategory: slug for the subcategory which has the tutorial series
    :return:
    """
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=slug_subcategory)

    tutorial_series = Tutorial.objects.filter(tutorial_category=subcategory)
    num_id = subcategory.classification.slug

    print(category)
    print(subcategory)
    print(subcategory.classification)
    print(num_id)
    print(tutorial_series)

    # print(tutorial_series)

    context = {
        "subcategory":subcategory,
        "tutorialseries":tutorial_series,
        "category":category,
    }

    for tut in tutorial_series:
        print(tut.title)

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

    return render(request=request, context=context, template_name="catalogue/alltutorialserieslist.html")






