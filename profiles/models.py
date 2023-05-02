from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.profile_name:
            self.profile_name = self.owner.username
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)