from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from core.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_teacher",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Others"), {"fields": ("groups", "user_permissions",)}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_teacher")
    list_filter = ("is_teacher", "is_staff", "is_superuser", "is_active", "groups")

