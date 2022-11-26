from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def job_listing(request):
    return render(request, 'job-listings.html')

def job(request):
    return render(request, 'job.html')

def job_single(request):
    return render(request, 'job-single.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def post_job(request):
    return render(request, 'post-job.html')