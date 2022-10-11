from django.contrib import admin
from . import models

# Register the `Post` model
admin.site.register(models.Post)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',


    )


admin.site.register(models.Post, PostAdmin)
