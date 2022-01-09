from django.urls import path
from .views import index, admin_login, user_login, recruiter_login, user_signup, user_home, Logout, recruiter_signup, admin_home,view_users, delete_user, recruiter_pending, change_status,recruiter_accepted,recruiter_rejected, recruiter_all, delete_recruiter

app_name = 'job'
urlpatterns = [
    path('', index, name='index'),    
    path('admin_login', admin_login, name='admin_login'),    
    path('user_login', user_login, name='user_login'),    
    path('recruiter_login', recruiter_login, name='recruiter_login'),    
    path('user_signup', user_signup, name='user_signup'),    
    path('user_home', user_home, name='user_home'),    
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
    path('Logout', Logout, name='Logout'),    
]