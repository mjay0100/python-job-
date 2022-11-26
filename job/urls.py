from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('job-listings/', views.job_listing),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('login/', views.login),
    path('job/job-single/', views.job_single),
    path('post-job/', views.post_job),
    path('students/', views.students),

    ]