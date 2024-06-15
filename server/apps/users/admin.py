from django.contrib import admin

from .models import CustomUser, EmployerProfile, JobSeekerProfile
admin.site.register(CustomUser)
admin.site.register(EmployerProfile)
admin.site.register(JobSeekerProfile)