# Generated by Django 4.0.2 on 2022-02-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.UUIDField()),
                ('doctor_name', models.CharField(max_length=25)),
                ('specialization', models.CharField(max_length=25)),
            ],
        ),
    ]
