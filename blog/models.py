from django.conf import settings
from django.db import models

# Create your models here.


# class PostQuerySet(models.QuerySet):
#     def published(self):
#         return self.filter(status=self.model.PUBLISHED)

#     def drafts(self):
#         return self.filter(status=self.model.DRAFT)


class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        null=False,
        unique_for_date='published',

    )

    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blog_posts',
        null=False,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published'
    )
    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )

    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    # objects = PostQuerySet.as_manager()
