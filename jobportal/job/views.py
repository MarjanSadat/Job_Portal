from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'job/index.html')

def admin_login(request):
    return render(request, 'job/admin_login.html')

def user_login(request):
    return render(request, 'job/user_login.html')

def recruiter_login(request):
    return render(request, 'job/recruiter_login.html')