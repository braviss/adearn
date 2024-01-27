from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models
from adearn import settings


# Create your models here.
class Article(models.Model):

    STATUS_ARTICLE_CHOICES = [
        ("pe", "Pending"),
        ("pu", "Published"),
        ("re", "Rejected"),
    ]

    title = models.CharField(max_length=200, blank=False, null=False)
    body = tinymce_models.HTMLField()
    status = models.CharField(max_length=2, choices=STATUS_ARTICLE_CHOICES, default='pe')
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='article_image/', null=True, blank=True, default='article_image/default.webp')
    tag = models.ManyToManyField('Tag', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name