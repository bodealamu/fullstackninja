from catalogue.models import Tutorial, TutorialVideo, Category, SubCategory
from django import forms


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ["title","description","tutorial_category","author","tutorial_logo","github_repo_link"]


class TutorialVideoForm(forms.ModelForm):
    class Meta:
        model = TutorialVideo
        fields = ["video_title", "description", "tutorial_category", "author", "youtube_link"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title","author","description","category_image"]


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["title","author","description","category", "subcategory_logo"]





