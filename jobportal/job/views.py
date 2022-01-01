from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def index(request):
    return render(request, 'job/index.html')

def admin_login(request):
    return render(request, 'job/admin_login.html')

def user_login(request):
    return render(request, 'job/user_login.html')

def recruiter_login(request):
    return render(request, 'job/recruiter_login.html')

def user_signup(request):
    error = ''

    if request.method == 'POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        i = request.POST.get('image')
        p = request.POST.get('pwd')
        e = request.POST.get('email')
        con = request.POST.get('contact')
        gen = request.POST.get('gender')
        try:
            user = User.objects.create_user(first_name = f,last_name = l,username=e, password = p)
            StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen,type='student')
            error = 'no'
        except:
            error = 'yes'
    d = {'error' : error}
    return render(request, 'job/user_signup.html', d)