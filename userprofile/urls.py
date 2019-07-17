# /userprofile/urls.py

from django.urls import path

import userprofile
from . import views

app_name = 'userprofile'

urlpatterns = [

path('login/', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),

# path('index/',index),

]