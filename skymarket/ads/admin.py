from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "author",
        "text"
    )
    readonly_fields = (
        "author",
        "ad"
    )


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "author",
        "title",
        "image",
        "price"
    )
    readonly_fields = (
        "author",
    )
