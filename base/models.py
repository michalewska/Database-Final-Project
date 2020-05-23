from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.

class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, null=True)
    start_time = models.CharField(max_length=10, null=True)
    end_time = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20, unique=True)
    start_time = models.CharField(max_length=10, null=True)
    end_time = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    deadline = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    start_time = models.CharField(max_length=10, null=True)
    end_time = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"