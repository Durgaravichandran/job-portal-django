from django.urls import path

from .views import (
    apply_for_job,
    my_applications,
    view_applicants,
    update_application_status,
)

urlpatterns = [

    path(
        'apply/<int:job_id>/',
        apply_for_job,
        name='apply_for_job'
    ),

    path(
        'my-applications/',
        my_applications,
        name='my_applications'
    ),

    path(
        'applicants/<int:job_id>/',
        view_applicants,
        name='view_applicants'
    ),

    path(
        'update-status/<int:application_id>/',
        update_application_status,
        name='update_application_status'
    ),
]