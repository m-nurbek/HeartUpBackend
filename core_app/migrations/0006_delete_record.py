# Generated by Django 5.0.3 on 2024-03-27 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_remove_patient_record_id_record_patient_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Record',
        ),
    ]
