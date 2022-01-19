from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import date
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
        u =  request.POST.get('uname')
        p =  request.POST.get('pwd')
        user = authenticate(username = u, password = p)
        if user:
            try:
                user1 = Recruiter.objects.get(user = user)
                print(user1.status)
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
    print(error)
    return render(request, 'job/recruiter_login.html',d)

def recruiter_signup(request):
    error = ''

    if request.method == 'POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        i = request.FILES.get('image')
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
        i = request.FILES.get('image')
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

    student = User.objects.get(id=pid)
    student.delete()
    return redirect('job:view_users')

def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    recruiter = User.objects.get(id=pid) 
    print(recruiter) 
    recruiter.delete()
    return redirect('job:recruiter_all')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    data = Recruiter.objects.filter(status='pending')
    d = {'data':data}

    return render(request, 'job/recruiter_pending.html',d)

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    error = ''
    recruiter = Recruiter.objects.get(id=pid)
    if request.method == 'POST':
        s = request.POST.get('status')
        recruiter.status = s
        try:
            recruiter.save()
            error = 'no'
        except:
            error = 'yes'

    d = {'recruiter':recruiter, 'error':error}

    return render(request, 'job/change_status.html',d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    error = ''
    if request.method == 'POST':
        c = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'

    d = {'error':error}

    return render(request, 'job/change_passwordadmin.html',d)

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('job:user_login')

    error = ''
    if request.method == 'POST':
        c = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'

    d = {'error':error}

    return render(request, 'job/change_passworduser.html',d)

def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')

    error = ''
    if request.method == 'POST':
        c = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'

    d = {'error':error}

    return render(request, 'job/change_passwordrecruiter.html',d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    data = Recruiter.objects.filter(status='Accept')
    d = {'data':data}

    return render(request, 'job/recruiter_accepted.html',d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    data = Recruiter.objects.filter(status='Reject')
    d = {'data':data}

    return render(request, 'job/recruiter_rejected.html',d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')

    data = Recruiter.objects.all()
    d = {'data':data}

    return render(request, 'job/recruiter_all.html',d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')

    user = request.user
    recruiter = Recruiter.objects.get(user=user)

    error = ''

    if request.method == 'POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        con = request.POST.get('contact')
        gen = request.POST.get('gender')

        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.mobile = con
        recruiter.gender = gen

        try:
            recruiter.save()
            recruiter.user.save()
            error = 'no'
        except:
            error = 'yes'
       
        i = request.FILES.get('image')       
        if i and i != None:           
            recruiter.image = i
            recruiter.save()
            error = 'no'
        

    d = {'recruiter':recruiter, 'error':error}
    return render(request, 'job/recruiter_home.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('job:user_login')

    user = request.user
    student = StudentUser.objects.get(user=user)

    error = ''

    if request.method == 'POST':
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        con = request.POST.get('contact')
        gen = request.POST.get('gender')

        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen

        try:
            student.save()
            student.user.save()
            error = 'no'
        except:
            error = 'yes'
       
        i = request.FILES.get('image')       
        if i and i != None:           
            student.image = i
            student.save()
            error = 'no'
        

    d = {'student':student, 'error':error}
    
    return render(request, 'job/user_home.html',d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('job:admin_login')
    return render(request, 'job/admin_home.html')

def Logout(request):
    logout(request)
    return redirect('job:index')

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')
    
    error = ''
    if request.method == 'POST':
        jt = request.POST.get('jobtitle')
        sd = request.POST.get('startdate')
        ed = request.POST.get('enddate')
        sal = request.POST.get('salary')
        l = request.FILES.get('logo')
        exp = request.POST.get('experience')
        loc = request.POST.get('location')
        skills = request.POST.get('skills')
        des = request.POST.get('description')
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter,start_date=sd,end_date=ed,title=jt,salary=sal,image=l,description=des,experience=exp,location=loc,skills=skills,creationdate=date.today())
            error = 'no'
        except:
            error = 'yes'
    d = {'error' : error}
    return render(request, 'job/add_job.html',d)


def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')

    error = ''
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST.get('jobtitle')
        sd = request.POST.get('startdate')
        ed = request.POST.get('enddate')
        sal = request.POST.get('salary')
        # l = request.FILES.get('logo')
        exp = request.POST.get('experience')
        loc = request.POST.get('location')
        skills = request.POST.get('skills')
        des = request.POST.get('description')

        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des

        try:
            job.save()
            error = 'no'
        except:
            error = 'yes'
        
        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass
            
        if ed:
            try:
                job.end_date = ed
                job.save()
            except:
                pass
        else:
            pass

    d = {'error' : error,'job':job}
    return render(request, 'job/edit_jobdetail.html',d)

def change_companylogo(request,pid):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')

    error = ''
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        cl = request.FILES.get('logo')
      
        job.image = cl

        try:
            job.save()
            error = 'no'
        except:
            error = 'yes'
        
       
    d = {'error' : error,'job':job}
    return render(request, 'job/change_companylogo.html',d)


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('job:recruiter_login')
    
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job':job}
    return render(request, 'job/job_list.html',d)


def latest_jobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job':job}
    return render(request, 'job/latest_jobs.html',d)

def user_latestjobs(request):
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li = []
    for i in data:
        li.append(i.job.id)
    
    d = {'job':job,'li':li}
    return render(request, 'job/user_latestjobs.html',d)

def job_detail(request, pid):
    job = Job.objects.get(id=pid)
    d = {'job':job}
    
    return render(request,'job/job_detail.html',d)