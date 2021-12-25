from django.urls import path
from .views import index, admin_login

app_name = 'job'
urlpatterns = [
    path('', index, name='index'),    
    path('admin_login', admin_login, name='admin_login'),    
]