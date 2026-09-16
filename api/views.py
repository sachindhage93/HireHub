from rest_framework import generics

from jobs.models import Job
from companies.models import Company
from applications.models import Application

from .serializers import (
    JobSerializer,
    CompanySerializer,
    ApplicationSerializer
)


class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.select_related(
        'company',
        'recruiter'
    ).all().order_by('-created_at')

    serializer_class = JobSerializer


class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.select_related(
        'company',
        'recruiter'
    ).all()

    serializer_class = JobSerializer


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.select_related(
        'recruiter'
    ).all().order_by('-created_at')

    serializer_class = CompanySerializer


class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.select_related(
        'recruiter'
    ).all()

    serializer_class = CompanySerializer


class ApplicationListAPIView(generics.ListAPIView):
    queryset = Application.objects.select_related(
        'seeker',
        'job'
    ).all().order_by('-applied_at')

    serializer_class = ApplicationSerializer


class ApplicationDetailAPIView(generics.RetrieveAPIView):
    queryset = Application.objects.select_related(
        'seeker',
        'job'
    ).all()

    serializer_class = ApplicationSerializer