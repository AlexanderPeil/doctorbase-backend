from rest_framework import serializers
from .models import Patient, Doctor, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
        extra_kwargs = {
                'b_date': {'input_formats': ['%Y-%m-%d', '%d-%m-%Y']}
        }

