# Generated by Django 5.0.6 on 2024-06-15 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobOpening',
            new_name='JobDetails',
        ),
        migrations.RenameField(
            model_name='jobapplication',
            old_name='job_opening',
            new_name='job_details',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_seeker',
        ),
    ]
