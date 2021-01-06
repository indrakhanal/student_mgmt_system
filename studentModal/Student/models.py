from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    fullname = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=15, null=True, blank=True)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    level = models.CharField(max_length=20, null=True, blank=True)
    college_name = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class News(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    file = models.FileField(upload_to='profile/', null=True, blank=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

