from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) # returns the current datetime in a timezone-aware format.
    created = models.DateTimeField(auto_now_add=True) # the date will be saved automatically when creating an object.
    updated = models.DateTimeField(auto_now=True)  # the date will be updated automatically when saving an object.
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title