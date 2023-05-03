from django.db import models
from django.contrib.auth.models import User
from .choices import LANGUAGE_CHOICES, CONFIDENCE_LEVEL


class Language(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=25,
        choices=LANGUAGE_CHOICES,
        blank=True,
        )
    confidence = models.CharField(
        max_length=25,
        choices=CONFIDENCE_LEVEL,
        blank=True,
        )
    used_since = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-confidence']

    def __str__(self):
        return f"{self.owner}'s {self.language} experience"
