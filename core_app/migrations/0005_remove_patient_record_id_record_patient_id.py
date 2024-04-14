# Generated by Django 5.0.3 on 2024-03-24 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0004_patient_record_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='record_id',
        ),
        migrations.AddField(
            model_name='record',
            name='patient_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core_app.patient'),
            preserve_default=False,
        ),
    ]
