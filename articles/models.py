from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Add later
    """
    LANGUAGE_CHOICES = (
    ('javascript', 'JavaScript'),
    ('python', 'Python'),
    ('java', 'Java'),
    ('c++', 'C++'),
    ('c#', 'C#'),
    ('typescript', 'TypeScript'),
    ('ruby', 'Ruby'),
    ('swift', 'Swift'),
    ('go', 'Go'),
    ('kotlin', 'Kotlin'),
    ('rust', 'Rust'),
    ('php', 'PHP'),
    ('perl', 'Perl'),
    ('html', 'HTML'),
    ('css', 'CSS'),
)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    art_title = models.CharField(max_length=255)
    art_content = models.TextField(blank=True)
    primary_language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,
    )
    github_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.art_title}'