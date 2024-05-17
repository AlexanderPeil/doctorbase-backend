from django.contrib import admin
from doctorbase_backend.models import Patient, Doctor, Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)