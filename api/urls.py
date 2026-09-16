from django.urls import path

from . import views


urlpatterns = [
    path(
        'jobs/',
        views.JobListAPIView.as_view(),
        name='api_jobs'
    ),

    path(
        'jobs/<int:pk>/',
        views.JobDetailAPIView.as_view(),
        name='api_job_detail'
    ),

    path(
        'companies/',
        views.CompanyListAPIView.as_view(),
        name='api_companies'
    ),

    path(
        'companies/<int:pk>/',
        views.CompanyDetailAPIView.as_view(),
        name='api_company_detail'
    ),

    path(
        'applications/',
        views.ApplicationListAPIView.as_view(),
        name='api_applications'
    ),

    path(
        'applications/<int:pk>/',
        views.ApplicationDetailAPIView.as_view(),
        name='api_application_detail'
    ),
]