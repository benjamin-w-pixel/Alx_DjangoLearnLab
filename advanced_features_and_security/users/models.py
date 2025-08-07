from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
import os
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    # Remove username, use email instead
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
    # Add custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos/", 
        null=True, 
        blank=True
    )

    USERNAME_FIELD = "email"       # Email is the login identifier
    REQUIRED_FIELDS = []           # No additional required fields

    objects = CustomUserManager()

    def __str__(self):
        return self.email