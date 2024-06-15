from django.contrib import admin

from .models import CustomUser, EmployerProfile, ApplicantProfile
admin.site.register(CustomUser)
admin.site.register(EmployerProfile)
admin.site.register(ApplicantProfile)