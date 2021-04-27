from django.db import models
from django.contrib.auth.models import User


# Create your models here.

BLOODGROUP_CHOICES = [
    ('AB-','AB-'),
    ('AB','AB'),
    ('AB+','AB+'),
    ('A-','A-'),
    ('A','A'),
    ('A+','A+'),
    ('B-','B-'),
    ('B','B'),
    ('B+','B+'),
    ('O-','O-'),
    ('O','O'),
    ('O+','O+'),
    ('ANY','ANY'),
]


STATUS_CHOICES = [
    ('O', 'Open'),
    ('C', 'Closed'),
]

VERIFIED_CHOICES = [
    ('U', 'Unverified'),
    ('V', 'Verified'),
    ('F', 'Fake')
]

class Requirements(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class CovidHelp(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_contact_no = models.CharField(max_length=15)
    patient_email=models.EmailField(blank=True)
    patient_age = models.CharField(max_length=3)
    patient_blood_group = models.CharField(max_length=3, choices = BLOODGROUP_CHOICES, default="ANY")
    patient_sp02_level = models.CharField(max_length=2)
    patient_requirements = models.ForeignKey(Requirements, on_delete=models.CASCADE, null=True, blank=True)


    alternate_contact = models.CharField(blank=True, max_length=100)
    alternate_contact_no = models.CharField(blank=True, max_length=15)

    location_city = models.CharField(max_length=30, help_text="The city where the patient needs help")
    location_hospital=models.CharField(blank=True, max_length=100, help_text="If the patient is aleady in a hospital")

    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default="O")
    date = models.DateTimeField(auto_now=True)

    additional_text = models.TextField(blank=True, help_text="Any additional details you may want to give")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.patient_name


    class Meta:
        ordering = ["patient_requirements","-date"]

class Available(models.Model):
    type = models.ForeignKey(Requirements, on_delete=models.CASCADE, null=True, blank=True)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    location = models.CharField(max_length=30)
    verified = models.CharField(max_length=1, choices=VERIFIED_CHOICES, default='U')
    last_verified = models.DateTimeField(auto_now=True)
    additional_text=models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_name

    class Meta:
        ordering =["type","-last_verified"]


class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['category','name']
