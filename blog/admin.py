from django.contrib import admin
from . import models
# from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [

        'title',
        'created',
        'updated',
        'author',

    ]

    search_fields = [
        'title',
        'author__username',
        'author__first_name',
        'author__last_name'



    ]


# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
