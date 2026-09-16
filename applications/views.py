from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Application
from .forms import ApplicationForm
from jobs.models import Job


@login_required
def apply_job(request, job_id):

    if request.user.profile.user_type != 'job_seeker':
        return redirect('role_home')

    job = get_object_or_404(
        Job,
        id=job_id
    )

    already_applied = Application.objects.filter(
        seeker=request.user,
        job=job
    ).exists()

    if already_applied:
        messages.warning(
            request,
            'You have already applied for this job.'
        )

        return redirect(
            'job_detail',
            job_id=job.id
        )

    if request.method == 'POST':

        form = ApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(commit=False)

            application.seeker = request.user
            application.job = job
            application.save()

            messages.success(
                request,
                'Application submitted successfully.'
            )

            return redirect(
                'my_applications'
            )

    else:

        form = ApplicationForm()

    return render(
        request,
        'applications/apply_job.html',
        {
            'form': form,
            'job': job
        }
    )


@login_required
def my_applications(request):

    if request.user.profile.user_type != 'job_seeker':
        return redirect('role_home')

    applications = Application.objects.filter(
        seeker=request.user
    ).select_related(
        'job',
        'job__company'
    ).order_by(
        '-applied_at'
    )

    return render(
        request,
        'applications/my_applications.html',
        {
            'applications': applications
        }
    )


@login_required
def recruiter_applications(request):

    if request.user.profile.user_type != 'recruiter':
        return redirect('role_home')

    applications = Application.objects.filter(
        job__recruiter=request.user
    ).select_related(
        'seeker',
        'job',
        'job__company'
    ).order_by(
        '-applied_at'
    )

    return render(
        request,
        'applications/recruiter_applications.html',
        {
            'applications': applications
        }
    )


@login_required
def update_application_status(
    request,
    application_id
):

    if request.user.profile.user_type != 'recruiter':
        return redirect('role_home')

    application = get_object_or_404(
        Application,
        id=application_id,
        job__recruiter=request.user
    )

    if request.method == 'POST':

        status = request.POST.get('status')

        valid_statuses = [
            'pending',
            'shortlisted',
            'rejected',
            'selected'
        ]

        if status in valid_statuses:

            application.status = status
            application.save()

            messages.success(
                request,
                'Application status updated successfully.'
            )

    return redirect(
        'recruiter_applications'
    )