from django.contrib import admin
from .models import Doctor, Patient, Appointment

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'b_date')
    inlines = [AppointmentInline]

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('title', 'firstname', 'lastname', 'speciality')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'doctor', 'patient')
    list_filter = ('doctor', 'patient', 'date')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
