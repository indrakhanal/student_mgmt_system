from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    fullname = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    qualification = models.CharField(max_length=20, null=True, blank=True)
    skill = models.CharField(max_length=20, null=True, blank=True)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FirstSem(models.Model):
    addNote = models.TextField(null=True, blank=True)
    assignment = models.CharField(max_length=50, null=True, blank=True)
    addFile = models.FileField(upload_to='profile/', null=True, blank=True)