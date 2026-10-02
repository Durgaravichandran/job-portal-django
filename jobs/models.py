from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):

    JOB_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
    )

    title = models.CharField(max_length=200)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    posted_by = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='posted_jobs',
    null=True,
    blank=True
   )
    description = models.TextField()

    location = models.CharField(max_length=100)

    salary = models.CharField(
        max_length=100,
        blank=True
    )

    experience = models.CharField(
        max_length=100,
        blank=True
    )

    skills = models.CharField(
        max_length=300
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title