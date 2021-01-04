from django.contrib import admin
from catalogue.models import Tutorial, TutorialVideo, Category, SubCategory, Courses

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(TutorialVideo)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Courses)
