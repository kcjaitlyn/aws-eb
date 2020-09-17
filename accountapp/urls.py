from django.contrib import admin
from django.urls import path
import accountapp.views

urlpatterns = [
    path('login/', accountapp.views.login, name='login'),
    path('signup/', accountapp.views.signup, name='signup'),
    path('logout/', accountapp.views.login, name='logout'),
]