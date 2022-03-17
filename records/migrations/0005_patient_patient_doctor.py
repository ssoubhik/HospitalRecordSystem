# Generated by Django 4.0.2 on 2022-03-17 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='records.doctor'),
        ),
    ]
