from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def index(request):
    return render(request, 'job/index.html')

def admin_login(request):
    return render(request, 'job/admin_login.html')

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = f = request.POST.get('uname')
        p = f = request.POST.get('pwd')
        user = authenticate(username = u, password = p)
        if user:
            try:
                user1 = StudentUser.objects.get(user = user)
                if user1.type == 'student':
                    login(request,user)
                    error = 'no'
                    return render(request, 'job/user_home.html')
                else:
                    error = 'yes'
            except:
                error = 'yes'
        else:
            error = 'yes'
    
    d = {'error' :error}

    return render(request, 'job/user_login.html', d)

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

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('job:user_login')
    return render(request, 'job/user_home.html')

def Logout(request):
    logout(request)
    return redirect('job:index')