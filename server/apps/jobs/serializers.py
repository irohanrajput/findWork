from rest_framework import serializers
from .models import JobDetails, JobApplication
from apps.users.models import ApplicantProfile


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    applicant_user_id = serializers.ReadOnlyField(source="applicant.user.id")
    applicant_profile_id = serializers.ReadOnlyField(source="applicant.id")
    print(applicant_profile_id)
    class Meta:
        model = JobApplication
        exclude = ['applicant']
        extra_kwargs = {
            "status": {"read_only": True},
            "applied_at": {"read_only": True},
        }
        

    def create(self, validated_data):
        request = self.context.get("request")
        try:
            applicant_profile = ApplicantProfile.objects.get(user=request.user)
            print(applicant_profile, request.user)
        except ApplicantProfile.DoesNotExist:
            raise serializers.ValidationError("Applicant profile does not exist")

        job_application = JobApplication.objects.create(
            job_id=validated_data["job_id"],
            applicant=applicant_profile,
            cover_letter=validated_data["cover_letter"],
            status="Pending",
        )
        return job_application
