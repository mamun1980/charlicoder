from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CharliUserCreationForm, CharliUserChangeForm
from .models import CharliUser


class CustomUserAdmin(UserAdmin):
    add_form = CharliUserCreationForm
    form = CharliUserChangeForm
    model = CharliUser
    list_display = ("email", "mobile", "is_staff", "is_active",)
    list_filter = ("email", "mobile", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "mobile", "password")}),
        ("Bio", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff",
         "is_active",  "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "mobile", "password1", "password2", "is_staff",
                "is_active", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CharliUser, CustomUserAdmin)