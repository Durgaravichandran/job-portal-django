from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .forms import RegistrationForm, ProfileForm


def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = RegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'accounts/login.html'
    )


def user_logout(request):

    logout(request)

    return redirect('login')


@login_required
def dashboard(request):

    # Superuser/admin does not need a Profile
    if request.user.is_superuser:
        return redirect('/admin/')

    # Normal users must have a Profile
    profile = request.user.profile

    if profile.user_type == 'job_seeker':

        return render(
            request,
            'accounts/job_seeker_dashboard.html'
        )

    if profile.user_type == 'employer':

        return render(
            request,
            'accounts/employer_dashboard.html'
        )

    return redirect('login')
@login_required
def profile(request):

    user_profile = request.user.profile

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:

        form = ProfileForm(
            instance=user_profile
        )

    return render(
        request,
        'accounts/profile.html',
        {
            'form': form
        }
    )