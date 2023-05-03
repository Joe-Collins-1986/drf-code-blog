from django.db import models
from django.contrib.auth.models import User
from languages.choices import LANGUAGE_CHOICES


class Article(models.Model):
    """
    Add later
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    art_title = models.CharField(max_length=255)
    art_content = models.TextField(blank=True)
    primary_language = models.CharField(
        max_length=25,
        choices=LANGUAGE_CHOICES,
        blank=True,
    )
    github_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.art_title}'