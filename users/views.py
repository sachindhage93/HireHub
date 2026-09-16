from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import ProfileForm


@login_required
def role_home(request):

    if not hasattr(request.user, 'profile'):
        return HttpResponse(
            'Profile not found.'
        )

    user_type = request.user.profile.user_type

    if user_type == 'job_seeker':

        return render(
            request,
            'users/seeker_home.html'
        )

    elif user_type == 'recruiter':

        return render(
            request,
            'users/recruiter_home.html'
        )

    else:

        return HttpResponse(
            'Invalid user role.'
        )


@login_required
def profile_view(request):

    profile = request.user.profile

    return render(
        request,
        'users/profile.html',
        {
            'profile': profile
        }
    )


@login_required
def profile_edit(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect('profile')

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'users/profile_edit.html',
        {
            'form': form
        }
    )