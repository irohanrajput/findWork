from django.db import models
from apps.users.models import EmployerProfile, ApplicantProfile

class JobDetails(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job_id = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected')], default='Pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_seeker.user.username} - {self.job_opening.title}"
