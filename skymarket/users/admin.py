from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "role"
    )
    readonly_fields = (
        "email",
    )
    filter_horizontal = ()
    list_filter = ()
    ordering = ("email",)
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "role"
                )
            }
        ),
    )


admin.site.unregister(Group)
