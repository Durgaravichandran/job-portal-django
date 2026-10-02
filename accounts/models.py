from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    USER_TYPES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    skills = models.CharField(
        max_length=300,
        blank=True
    )

    education = models.CharField(
        max_length=300,
        blank=True
    )

    experience = models.CharField(
        max_length=300,
        blank=True
    )

    resume = models.FileField(
        upload_to='profile_resumes/',
        blank=True
    )

    def __str__(self):
        return self.user.username