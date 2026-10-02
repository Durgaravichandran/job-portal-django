from django.urls import path

from .views import (
    job_list,
    job_detail,
    post_job,
    my_jobs,
)


urlpatterns = [

    path(
        '',
        job_list,
        name='job_list'
    ),

    path(
        'post/',
        post_job,
        name='post_job'
    ),

    path(
        'my-jobs/',
        my_jobs,
        name='my_jobs'
    ),

    path(
        '<int:job_id>/',
        job_detail,
        name='job_detail'
    ),
]