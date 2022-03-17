from django.db import models


# Create your models here.

# doctor model
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=25)
    specialization = models.CharField(max_length=25)

    def __str__(self):
        return self.doctor_name


# patient model
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=25)
    patient_dob = models.DateField()
    patient_address = models.CharField(max_length=100)
    patient_date_admitted = models.DateTimeField()
    patient_doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.patient_name
