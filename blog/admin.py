from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_filter = ("created_time",)


admin.site.unregister(Group)
admin.site.register(User)