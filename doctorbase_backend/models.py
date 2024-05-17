from django.db import models
from django.conf import settings
from datetime import date


class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} {self.user.username}"


class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    b_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descritpion = models.CharField(max_length=500)
    date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment: {self.title} on {self.date}"