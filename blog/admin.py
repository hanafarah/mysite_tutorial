from django.contrib import admin
from . import models
# from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',


    )


search_fields = (
    'title',
)

# Register the `Post` model
admin.site.register(models.Post)
