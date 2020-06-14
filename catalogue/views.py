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


def subcategories_list(request, slug_subcategory):
    """
    A list view for all the subcategories
    :param request:
    :param slug_subcategory: str, url slug for the chosen subcategory
    :return:
    """

    subcategories = SubCategory.objects.filter(category=slug_subcategory)

    context = {
        "subcategories":subcategories,
    }

    return render(request=request, template_name="catalogue/subcategorieslist.html", context=context)



