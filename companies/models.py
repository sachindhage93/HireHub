from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    location = models.CharField(
        max_length=100
    )

    logo = models.ImageField(
        upload_to='company_logos/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name