# Generated by Django 5.0.3 on 2024-05-03 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0019_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='alcoholic',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='heart_disease',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hypertension',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='smoker',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='weight',
        ),
    ]
