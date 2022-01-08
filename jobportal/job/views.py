from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def index(request):
    return render(request, 'job/index.html')

def admin_login(request):
    error = ''
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pwd')
        user = authenticate(username =u, password=p)
        print(u,p)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    
    d = {'error':error}

    return render(request, 'job/admin_login.html',d)

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pwd')
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
    error = ""
    if request.method == 'POST':
        u = f = request.POST.get('uname')
        p = f = request.POST.get('pwd')
        user = authenticate(username = u, password = p)
        if user:
            try:
                user1 = Recruiter.objects.get(user = user)
                if user1.type == 'recruiter' and user1.status != 'pending':
                    login(request,user)
                    error = 'no'
                    # return render(request, 'job/user_home.html')
                else:
                    error = 'not'
            except:
                error = 'yes'
        else:
            error = 'yes'
    
    d = {'error' :error}

    return render(request, 'job/recruiter_login.html',d)

def recruiter_signup(request):
    error = ''

    if request.method == 'POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        i = request.POST.get('image')
        p = request.POST.get('pwd')
        e = request.POST.get('email')
        con = request.POST.get('contact')
        gen = request.POST.get('gender')
        company = request.POST.get('company')
        try:
            user = User.objects.create_user(first_name = f,last_name = l,username=e, password = p)
            Recruiter.objects.create(user=user,mobile=con,image=i,gender=gen,company=company,type='recruiter',status='pending')
            error = 'no'
        except:
            error = 'yes'
    d = {'error' : error}

    return render(request, 'job/recruiter_signup.html',d)

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


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request, 'job/view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    student = StudentUser.objects.get(id=pid)
    print(student)
    student.delete()
    return redirect('job:view_users')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    data = Recruiter.objects.filter(status='pending')
    d = {'data':data}

    return render(request, 'job/recruiter_pending.html',d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')
    return render(request, 'job/recruiter_home.html')


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('job:user_login')
    return render(request, 'job/user_home.html')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')
    return render(request, 'job/admin_home.html')

def Logout(request):
    logout(request)
    return redirect('job:index')