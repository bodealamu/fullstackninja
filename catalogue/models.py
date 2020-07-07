from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    """Database model which represents Category objects"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, unique=True, verbose_name="Name of Category")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Describe what this section is about.")
    category_image = models.ImageField(verbose_name="Logo for this category", upload_to="images/Category/",
                                       max_length=200, blank=False)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): # new

        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class SubCategory(models.Model):
    """Database model for subcategories"""
    id = models.AutoField(primary_key=True)
    classification = models.ForeignKey(to=Category, on_delete=models.CASCADE,
                                 verbose_name="What category does this belong?")
    subcategory_logo = models.ImageField(upload_to="images/Subcategory/", max_length=200,
                                         blank=False,verbose_name="Logo for the subcategory")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Describe what this section is about.")
    title = models.CharField(max_length=40, unique=True, verbose_name="Name of Sub-Category")
    slug = models.SlugField(max_length=200, default="default_slug", unique=True)

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    """Database models for representing Tutorial objects."""
    id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name="Describe what this section is about.")
    title = models.CharField(max_length=40, unique=True, verbose_name="Name of Tutorial series")
    tutorial_category = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE,
                                          verbose_name="What subcategory does this tutorial belong?")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    tutorial_logo = models.ImageField(upload_to="images/Tutorial/", max_length=200,
                                      verbose_name="Logo for tutorial series", blank=False)
    github_repo_link = models.URLField(verbose_name="Link to github repo", max_length=150)
    tutorial_series_slug = models.SlugField(max_length=200, default="default_slug", unique=True)

    def __str__(self):
        return self.title


class TutorialVideo(models.Model):
    """Database models for representing tutorial video objects"""
    id = models.AutoField(primary_key=True)
    youtube_link = models.URLField(verbose_name="Youtube link for uploaded video", max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Describe what this section is about.")
    video_title = models.CharField(max_length=40, unique=True, verbose_name="Title of uploaded video",)
    tutorial_category = models.ForeignKey(to=Tutorial, on_delete=models.CASCADE,
                                          verbose_name="What Tutorial series does this belong?")
    tutorial_video_slug = models.SlugField(max_length=200, default="default_slug", unique=True)

    def __str__(self):
        return self.video_title


class Contact(models.Model):
    """Database models for representing messages sent through the contact page."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="Your full name (30 characters)")
    email = models.EmailField(max_length=50, verbose_name="Your email address")
    message = models.TextField(verbose_name="Message")
    message_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

