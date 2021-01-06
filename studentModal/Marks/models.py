from django.db import models
from django.contrib.auth.models import User


class SixthSem(models.Model):
    fullname = models.CharField(max_length=19, null=True, blank=True)
    roll_no = models.CharField(max_length=10, unique=True)
    webTech = models.IntegerField(null=True, blank=True)
    compiler = models.IntegerField(null=True, blank=True)
    rts = models.IntegerField(null=True, blank=True)
    software = models.IntegerField(null=True, blank=True)
    dot_net = models.IntegerField(null=True, blank=True)
    e_commerce = models.IntegerField(null=True, blank=True)

    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class FirstSem(models.Model):
    fullname = models.CharField(max_length=20, null=True, blank=True)
    roll = models.CharField(max_length=7, unique=True)
    Physics = models.IntegerField(null=True, blank=True)
    math = models.IntegerField(null=True, blank=True)
    C_programming = models.IntegerField(null=True, blank=True)
    Digital = models.IntegerField(null=True, blank=True)
    F_it = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fullname


class SecondSem(models.Model):
    fullname = models.CharField(max_length=20, null=True, blank=True)
    roll_no = models.CharField(max_length=5, unique=True)
    discrete = models.IntegerField(null=True, blank=True)
    math_ii = models.IntegerField(null=True, blank=True)
    micro = models.IntegerField(null=True, blank=True)
    stat_i = models.IntegerField(null=True, blank=True)
    oop = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fullname


class ThirdSem(models.Model):
    fullname = models.CharField(max_length=19, null=True, blank=True)
    roll_no = models.CharField(max_length=2, unique=True)
    dsa = models.IntegerField(null=True, blank=True)
    nm = models.IntegerField(null=True, blank=True)
    ca = models.IntegerField(null=True, blank=True)
    cg = models.IntegerField(null=True, blank=True)
    stat_ii = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fullname




