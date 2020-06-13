from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import CustomUser


# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("email", "first_name", "last_name", "is_superuser", "is_staff")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email","password")}),
        ("Personal info", {"fields":("first_name", "last_name")}),
        ("Permissions", {"fields":("is_superuser", "is_active", "is_staff")})
    )
    add_fieldsets = (
        (None, {
            "classes":('wide',),
            "fields":('email', 'first_name','last_name','password1', 'password2')
        }
         ),
    )


admin.site.register(CustomUser, UserAdmin)