# Generated by Django 5.0.6 on 2024-05-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorbase_backend', '0002_remove_doctor_user_doctor_firstname_doctor_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
    ]