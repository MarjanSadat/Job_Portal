from django.urls import path
from .views import index, admin_login, user_login, recruiter_login, user_signup

app_name = 'job'
urlpatterns = [
    path('', index, name='index'),    
    path('admin_login', admin_login, name='admin_login'),    
    path('user_login', user_login, name='user_login'),    
    path('recruiter_login', recruiter_login, name='recruiter_login'),    
    path('user_signup', user_signup, name='user_signup'),    
]