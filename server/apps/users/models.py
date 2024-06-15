from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    mobile = models.IntegerField(blank=True, null=True, unique=True)
    
    def __str__(self):
        return self.username
    
class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.company_name

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.user.username
