from django.contrib import admin
from . import models
# from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [

        'title',
        'created',
        'updated',
        'author',
        'slug',

    ]

    search_fields = [
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',


    ]

    list_filter = [
        'status',
    ]

    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {'slug': ('name',)}


# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
