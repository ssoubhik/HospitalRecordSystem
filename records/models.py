from django.db import models


# Create your models here.

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=25)
    specialization = models.CharField(max_length=25)

    def __str__(self):
        return self.doctor_name
