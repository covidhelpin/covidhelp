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
]

REQUIREMENT_CHOICES = [
    ('B', 'Bed'),
    ('I', 'ICU'),
    ('O', 'Oxygen'),
    ('P', 'Plasma'),
    ('R', 'Remidisiver'),
    ('F', 'Fabiflu'),
    ('M', 'Other Medicines'),
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

class CovidHelp(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_contact_no = models.CharField(max_length=10)
    patient_email=models.EmailField(blank=True)
    patient_age = models.CharField(max_length=3)
    patient_blood_group = models.CharField(max_length=3, choices = BLOODGROUP_CHOICES)
    patient_sp02_level = models.CharField(max_length=2)
    patient_requirements = models.CharField(max_length=1, choices = REQUIREMENT_CHOICES)

    alternate_contact = models.CharField(blank=True, max_length=100)
    alternate_contact_no = models.CharField(blank=True, max_length=10)

    location_city = models.CharField(max_length=30, help_text="The city where the patient needs help")
    location_hospital=models.CharField(blank=True, max_length=100, help_text="If the patient is aleady in a hospital")

    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default="O")
    date = models.DateTimeField(auto_now=True)

    additional_text = models.TextField(blank=True, help_text="Any additional details you may want to give")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.patient_name


    class Meta:
        ordering = ["-date"]

class Available(models.Model):
    type = models.CharField(max_length=1,choices = REQUIREMENT_CHOICES)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    location = models.CharField(max_length=30)
    verified = models.CharField(max_length=1, choices=VERIFIED_CHOICES, default='U')
    last_verified = models.DateTimeField(auto_now=True)
    additional_text=models.TextField(blank=True)

    def __str__(self):
        return self.contact_name

    class Meta:
        ordering =["-last_verified"]
