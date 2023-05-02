from django.db import models
from django.contrib.auth.models import User
from articles.models import Article


class Like(models.Model):
    """
    Add in later
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'article']

    def __str__(self):
        return f"Article: {self.article} by {self.owner}"
