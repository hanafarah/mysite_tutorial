from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=True
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
