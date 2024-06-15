# Generated by Django 5.0.6 on 2024-06-15 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='job_seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobseekerprofile'),
        ),
        migrations.AddField(
            model_name='jobopening',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employerprofile'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_opening',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobopening'),
        ),
    ]
