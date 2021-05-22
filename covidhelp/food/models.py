from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIFFIN_CHOICES = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class Volunteer(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    phone = models.CharField(max_length=15)
    pin_code = models.CharField(max_length=10)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name.username

class Customer(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    adhaar = models.CharField(max_length=12)
    phone = models.CharField(max_length=15)
    pin_code = models.CharField(max_length=10)
    tiffin_nos = models.CharField(max_length=1,choices=TIFFIN_CHOICES,default="1")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name.username

class Donor(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    phone = models.CharField(max_length=15)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name.username
