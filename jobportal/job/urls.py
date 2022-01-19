from django.urls import path
from .views import index, admin_login, user_login, recruiter_login, user_signup, user_home, Logout, recruiter_signup, admin_home,view_users, delete_user, recruiter_pending, change_status,recruiter_accepted,recruiter_rejected, recruiter_all, delete_recruiter, change_passwordadmin,change_passworduser, recruiter_home, change_passwordrecruiter, add_job, job_list, edit_jobdetail, change_companylogo, latest_jobs, user_latestjobs, job_detail

app_name = 'job'
urlpatterns = [
    path('', index, name='index'),    
    path('admin_login', admin_login, name='admin_login'),    
    path('user_login', user_login, name='user_login'),    
    path('recruiter_login', recruiter_login, name='recruiter_login'),    
    path('user_signup', user_signup, name='user_signup'),    
    path('user_home', user_home, name='user_home'),    
    path('recruiter_home', recruiter_home, name='recruiter_home'),    
    path('recruiter_signup', recruiter_signup, name='recruiter_signup'),    
    path('admin_home', admin_home, name='admin_home'),    
    path('view_users', view_users, name='view_users'),   
    path('recruiter_pending', recruiter_pending, name='recruiter_pending'),    
    path('recruiter_accepted', recruiter_accepted, name='recruiter_accepted'),    
    path('recruiter_rejected', recruiter_rejected, name='recruiter_rejected'),    
    path('recruiter_all', recruiter_all, name='recruiter_all'),    
    path('delete_user/<int:pid>', delete_user, name='delete_user'),    
    path('delete_recruiter/<int:pid>', delete_recruiter, name='delete_recruiter'),    
    path('change_status/<int:pid>', change_status, name='change_status'),    
    path('change_passwordadmin', change_passwordadmin, name='change_passwordadmin'),    
    path('change_passworduser', change_passworduser, name='change_passworduser'),    
    path('change_passwordrecruiter', change_passwordrecruiter, name='change_passwordrecruiter'),    
    path('add_job', add_job, name='add_job'),    
    path('job_list', job_list, name='job_list'), 
    path('latest_jobs', latest_jobs, name='latest_jobs'), 
    path('user_latestjobs', user_latestjobs, name='user_latestjobs'), 
    path('job_detail/<int:pid>', job_detail, name='job_detail'), 
    path('edit_jobdetail/<int:pid>', edit_jobdetail, name='edit_jobdetail'),       
    path('change_companylogo/<int:pid>', change_companylogo, name='change_companylogo'),       
    path('Logout', Logout, name='Logout'),    
]