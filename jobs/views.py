from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Job
from .forms import JobForm


def job_list(request):

    jobs = Job.objects.all().order_by('-created_at')

    search = request.GET.get('search')
    location = request.GET.get('location')

    if search:
        jobs = (
            jobs.filter(title__icontains=search)
            | jobs.filter(skills__icontains=search)
            | jobs.filter(company__name__icontains=search)
        )

    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': jobs,
            'search': search,
            'location': location
        }
    )


def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    return render(
        request,
        'jobs/job_detail.html',
        {
            'job': job
        }
    )


@login_required
def post_job(request):

    if request.user.profile.user_type != 'employer':
        return redirect('job_list')

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.posted_by = request.user

            job.save()

            return redirect('job_list')

    else:

        form = JobForm()

    return render(
        request,
        'jobs/post_job.html',
        {
            'form': form
        }
    )


@login_required
def my_jobs(request):

    if request.user.profile.user_type != 'employer':
        return redirect('job_list')

    jobs = Job.objects.filter(
        posted_by=request.user
    ).order_by('-created_at')

    return render(
        request,
        'jobs/my_jobs.html',
        {
            'jobs': jobs
        }
    )