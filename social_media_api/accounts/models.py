from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user extending AbstractUser.

    Fields:
    - bio: optional longer description
    - profile_picture: optional image
    - followers: many-to-many to self, asymmetrical (followers != following)
    """
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='following', blank=True
    )

    def __str__(self):
        return self.username