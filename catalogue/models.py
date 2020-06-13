from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, unique=True, verbose_name="Name of Category")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Describe what this section is about.")
    category_image = models.ImageField(verbose_name="Logo for this category", upload_to="images/Category/",
                                       max_length=200, blank=False)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE,
                                 verbose_name="What category does this belong?")
    subcategory_logo = models.ImageField(upload_to="images/Subcategory/", max_length=200,
                                         blank=False,verbose_name="Logo for the subcategory")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Describe what this section is about.")
    title = models.CharField(max_length=40, unique=True, verbose_name="Name of Sub-Category")

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name="Describe what this section is about.")
    title = models.CharField(max_length=40, unique=True, verbose_name="Name of Sub-Category")
    tutorial_category = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE,
                                          verbose_name="What category does this tutorial belong?")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    tutorial_logo = models.ImageField(upload_to="images/Tutorial/", max_length=200,
                                      verbose_name="Logo for tutorial series", blank=False)
    github_repo_link = models.URLField(verbose_name="Link to github repo", max_length=150)

    def __str__(self):
        return self.title


class TutorialVideo(models.Model):
    id = models.AutoField(primary_key=True)
    youtube_link = models.URLField(verbose_name="Youtube link for uploaded video", max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Describe what this section is about.")
    video_title = models.CharField(max_length=40, unique=True, verbose_name="Title of uploaded video",)
    tutorial_category = models.ForeignKey(to=Tutorial, on_delete=models.CASCADE,
                                          verbose_name="What Tutorial series does this belong?")

    def __str__(self):
        return self.video_title

