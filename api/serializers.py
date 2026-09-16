from rest_framework import serializers

from jobs.models import Job
from companies.models import Company
from applications.models import Application


class CompanySerializer(serializers.ModelSerializer):
    recruiter_username = serializers.CharField(
        source='recruiter.username',
        read_only=True
    )

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'description',
            'website',
            'location',
            'logo',
            'recruiter_username',
            'created_at',
        ]


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(
        source='company.name',
        read_only=True
    )

    recruiter_username = serializers.CharField(
        source='recruiter.username',
        read_only=True
    )

    job_type_display = serializers.CharField(
        source='get_job_type_display',
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'description',
            'requirements',
            'location',
            'salary',
            'job_type',
            'job_type_display',
            'experience_required',
            'deadline',
            'company',
            'company_name',
            'recruiter_username',
            'created_at',
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    seeker_username = serializers.CharField(
        source='seeker.username',
        read_only=True
    )

    job_title = serializers.CharField(
        source='job.title',
        read_only=True
    )

    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True
    )

    class Meta:
        model = Application
        fields = [
            'id',
            'seeker',
            'seeker_username',
            'job',
            'job_title',
            'cover_letter',
            'status',
            'status_display',
            'applied_at',
        ]