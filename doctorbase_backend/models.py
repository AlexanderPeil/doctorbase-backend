from django.db import models
from django.conf import settings
from datetime import date


class Doctor(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, default='Max')
    lastname = models.CharField(max_length=100, default='Mustermann')
    speciality = models.CharField(max_length=100)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} {self.firstname} {self.lastname}"


class Patient(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    b_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    @property
    def appointments(self):
        return self.appointment_set.all()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment: {self.title} on {self.date} with {self.patient.firstname} {self.patient.lastname}"