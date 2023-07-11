from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserProfile(AbstractUser):
    role_choices = (
        ('Agent', 'Agent'),
        ('Admin', 'Admin'),
        ('Blog Writer', 'Blog Writer'),
        ('Other', 'Other'),
    )

    status_choices = (
        ('Active', 'Active'),
        ('Banned', 'Banned'),
    )

    role = models.CharField(max_length=15, choices=role_choices)
    avatar = models.ImageField(blank=True, null=True)
    status = models.CharField(
        max_length=15, choices=status_choices, default="Active")
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=500, blank=True)
    bio = models.TextField(blank=True)
    facebook_link = models.CharField(max_length=250, blank=True)
    instagram_link = models.CharField(max_length=250, blank=True)
    website_link = models.CharField(max_length=250, blank=True)
    youtube_link = models.CharField(max_length=250, blank=True)
    twitter_link = models.CharField(max_length=250, blank=True)
    linkedin_link = models.CharField(max_length=250, blank=True)

    def __str__(self) -> str:
        return self.username
