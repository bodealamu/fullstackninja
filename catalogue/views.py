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


def tutorial_by_subcategory(request, slug_subcategory):
    subcategory = get_object_or_404(SubCategory, slug=slug_subcategory)
    print(subcategory)

    tutorial_series = Tutorial.objects.filter(tutorial_category=subcategory)


    # tutorial_series = Tutorial.objects.filter(tutorial_category=)

    context = {
        "tutorialseries":tutorial_series,
    }

    return render(request=request, context=context, template_name="catalogue/tutorialbysubcategory.html")


def tutorial_series_by_all_tutorials(request,   tutorial_series_slug):
    """
    :param request:
    :param slug_subcategory: slug for the subcategory which has the tutorial series
    :return:
    """
    print("im here")

    tutorial_series = get_object_or_404(Tutorial, tutorial_series_slug=tutorial_series_slug)
    print(tutorial_series)

    tutorial_videos = TutorialVideo.objects.filter(tutorial_category=tutorial_series)

    context = {
        "tutorialseries":tutorial_series,
    }

    return render(request=request, template_name="catalogue/t.html",context=context)





