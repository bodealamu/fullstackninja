from catalogue.models import Tutorial, TutorialVideo, Category, SubCategory
from django import forms


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ["title","description","tutorial_category","author","tutorial_logo","github_repo_link"]
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
            "github_repo_link": forms.TextInput(attrs={'class': 'form-control'}),

        }


class TutorialVideoForm(forms.ModelForm):
    class Meta:
        model = TutorialVideo
        fields = ["video_title", "description", "tutorial_category", "author", "youtube_link"]
        widgets = {
            "video_title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
            "youtube_link":forms.TextInput(attrs={'class':'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title","author","description","category_image"]
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
        }


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["title","author","description","classification", "subcategory_logo"]
        widgets = {
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
        }




