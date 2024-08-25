from django.db import models

from catalog.models import NULLABLE
from users.models import User


class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Title"
    )
    slug = models.CharField(
        max_length=200,
        verbose_name='slug',
        **NULLABLE
    )
    content = models.TextField(
        verbose_name="Content"
    )
    image = models.ImageField(
        upload_to="blog/image",
        **NULLABLE,
        verbose_name="Image"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Is published")
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Counter views",
        editable=False
    )
    owner = models.ForeignKey(
        User, verbose_name="Author",
        help_text="Please indicate the author of the post",
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]


class Version(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    number = models.PositiveIntegerField(verbose_name='Version number')
    is_current = models.BooleanField(default=False, verbose_name='Is current')

    product = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Post')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
