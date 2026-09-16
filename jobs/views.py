from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from .forms import JobForm, JobSearchForm
from .models import Job


@login_required
def job_create(request):

    if request.user.profile.user_type != 'recruiter':
        return redirect('role_home')

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.recruiter = request.user

            job.save()

            return redirect('job_list')

    else:
        form = JobForm()

    return render(
        request,
        'jobs/job_create.html',
        {'form': form}
    )


@login_required
def job_list(request):

    jobs = Job.objects.select_related(
        'company',
        'recruiter'
    ).all().order_by('-created_at')

    search_form = JobSearchForm(request.GET or None)

    q = request.GET.get('q', '').strip()
    location = request.GET.get('location', '').strip()
    job_type = request.GET.get('job_type', '').strip()
    company_id = request.GET.get('company', '').strip()

    # Keyword Search
    if q:
        jobs = jobs.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(requirements__icontains=q)
        )

    # Location Filter
    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    # Job Type Filter
    if job_type:
        jobs = jobs.filter(
            job_type=job_type
        )

    # Company Filter
    if company_id:
        jobs = jobs.filter(
            company_id=company_id
        )

    # Pagination
    paginator = Paginator(jobs, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': page_obj,
            'page_obj': page_obj,
            'search_form': search_form,
        }
    )


@login_required
def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    return render(
        request,
        'jobs/job_detail.html',
        {'job': job}
    )


@login_required
def job_edit(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    if request.method == 'POST':

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            return redirect(
                'job_detail',
                job_id=job.id
            )

    else:

        form = JobForm(
            instance=job
        )

    return render(
        request,
        'jobs/job_edit.html',
        {
            'form': form,
            'job': job
        }
    )


@login_required
def job_delete(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    if request.method == 'POST':

        job.delete()

        return redirect('job_list')

    return render(
        request,
        'jobs/job_delete.html',
        {'job': job}
    )