from rest_framework import serializers
from .models import JobOpening, JobApplication

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [   'job_opening', 'cover_letter',]
        
    def create(self, validated_data):
        request = self.context.get('request')
        job_seeker_profile = request.user.job_seeker_profile
        job_application = JobApplication.objects.create(job_seeker_profile=job_seeker_profile, **validated_data)
        
