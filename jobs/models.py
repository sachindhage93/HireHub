from django.db import models
from django.contrib.auth.models import User
from companies.models import Company


class Job(models.Model):

    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
    )

    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    requirements = models.TextField(
        blank=True
    )

    location = models.CharField(
        max_length=100
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES
    )

    experience_required = models.PositiveIntegerField(
        default=0
    )

    deadline = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title