from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from companies.models import Company
from applications.models import Application


@login_required
def dashboard_home(request):

    user_type = request.user.profile.user_type

    # Job Seeker Dashboard
    if user_type == 'job_seeker':

        total_applications = Application.objects.filter(
            seeker=request.user
        ).count()

        pending_applications = Application.objects.filter(
            seeker=request.user,
            status='pending'
        ).count()

        shortlisted_applications = Application.objects.filter(
            seeker=request.user,
            status='shortlisted'
        ).count()

        selected_applications = Application.objects.filter(
            seeker=request.user,
            status='selected'
        ).count()

        rejected_applications = Application.objects.filter(
            seeker=request.user,
            status='rejected'
        ).count()

        context = {
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'shortlisted_applications': shortlisted_applications,
            'selected_applications': selected_applications,
            'rejected_applications': rejected_applications,
        }

        return render(
            request,
            'dashboard/seeker_dashboard.html',
            context
        )

    # Recruiter Dashboard
    elif user_type == 'recruiter':

        total_companies = Company.objects.filter(
            recruiter=request.user
        ).count()

        total_jobs = Job.objects.filter(
            recruiter=request.user
        ).count()

        total_applications = Application.objects.filter(
            job__recruiter=request.user
        ).count()

        pending_applications = Application.objects.filter(
            job__recruiter=request.user,
            status='pending'
        ).count()

        shortlisted_applications = Application.objects.filter(
            job__recruiter=request.user,
            status='shortlisted'
        ).count()

        selected_applications = Application.objects.filter(
            job__recruiter=request.user,
            status='selected'
        ).count()

        rejected_applications = Application.objects.filter(
            job__recruiter=request.user,
            status='rejected'
        ).count()

        context = {
            'total_companies': total_companies,
            'total_jobs': total_jobs,
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'shortlisted_applications': shortlisted_applications,
            'selected_applications': selected_applications,
            'rejected_applications': rejected_applications,
        }

        return render(
            request,
            'dashboard/recruiter_dashboard.html',
            context
        )

    return render(
        request,
        'dashboard/dashboard.html'
    )