"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import *



urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name = "home"),
    

    path("login_page/", login_page, name = "login_page"),
    path("signup/", signup, name = "signup"),    
    path('dashboard/', dashboard, name ='dashboard'),
    path('reminders/', reminders, name='reminders'),
    path('add_reminder/', add_reminder, name='add_reminder'),
    path('calendar/', calendar, name='calendar'),
    path('settings/', settings, name='settings'),
    path('clients_due/', clients_due, name='clients_due'),
    path('client/', client_list, name='client_list'),
    path('client_details/<int:pk>/', client_details, name='client_details'),
    path('update_client/<int:pk>/', update_client, name='update_client'),
    path('delete_client/<int:pk>/', delete_client, name='delete_client'),
    path('add_client/', add_client, name='add_client'),
    path('templates/', templates, name = 'templates'),
    path('create_template/', create_template, name = 'create_template'),
    path('input_details/', input_details, name='input_details'),
    path('send_template/', send_template, name='send_template'),
    path('success/', success, name='success'), 
    path('reminder_success/', reminder_success, name='reminder_success'),
    path('detail/<int:pk>/', reminder_detail, name='reminder_detail'),
    
]

