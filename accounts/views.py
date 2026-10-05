from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm


def home_view(request):
    return render(request, 'accounts/home.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('role_home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('role_home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        selected_role = request.POST.get('selected_role', '')

        if selected_role not in ('job_seeker', 'recruiter'):
            messages.error(request, 'Please select Job Seeker or Recruiter.')
            return render(request, 'accounts/login.html')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')

        # Check the account role before creating a login session.
        profile = getattr(user, 'profile', None)
        if profile is None:
            messages.error(request, 'User profile not found. Please contact the administrator.')
            return render(request, 'accounts/login.html')

        if profile.user_type != selected_role:
            messages.error(
                request,
                'The selected login type does not match this account. Please choose the correct role.'
            )
            return render(request, 'accounts/login.html')

        login(request, user)
        messages.success(request, 'Login successful.')
        return redirect('role_home')

    return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out.')
    return redirect('login')
