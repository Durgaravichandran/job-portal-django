from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from jobs.models import Job
from .models import Application


@login_required
def apply_for_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    # Only job seekers can apply
    if request.user.profile.user_type != 'job_seeker':
        return redirect(
            'job_detail',
            job_id=job.id
        )

    # Check if the user already applied
    already_applied = Application.objects.filter(
        job=job,
        applicant=request.user
    ).exists()

    if already_applied:
        return render(
            request,
            'applications/already_applied.html',
            {
                'job': job
            }
        )

    # Submit application
    if request.method == 'POST':

        resume = request.FILES.get('resume')

        cover_letter = request.POST.get(
            'cover_letter',
            ''
        )

        Application.objects.create(
            job=job,
            applicant=request.user,
            resume=resume,
            cover_letter=cover_letter
        )

        return redirect(
            'my_applications'
        )

    return render(
        request,
        'applications/apply.html',
        {
            'job': job
        }
    )


@login_required
def my_applications(request):

    applications = Application.objects.filter(
        applicant=request.user
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
def view_applicants(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    # Only the employer who posted the job
    # can view its applicants
    if job.posted_by != request.user:
        return redirect(
            'my_jobs'
        )

    applications = Application.objects.filter(
        job=job
    ).select_related(
        'applicant'
    ).order_by(
        '-applied_at'
    )

    return render(
        request,
        'applications/view_applicants.html',
        {
            'job': job,
            'applications': applications
        }
    )
@login_required
def update_application_status(request, application_id):

    application = get_object_or_404(
        Application,
        id=application_id
    )

    # Only the employer who posted the job can update status
    if application.job.posted_by != request.user:
        return redirect('my_jobs')

    if request.method == 'POST':

        status = request.POST.get('status')

        if status in dict(Application.STATUS_CHOICES):
            application.status = status
            application.save()

    return redirect(
        'view_applicants',
        job_id=application.job.id
    )