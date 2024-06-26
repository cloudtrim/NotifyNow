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
    path('contacts/', contacts_list, name='contacts_list'),
    path('create_contact/', create_contact, name='create_contact'),
    path('templates/', templates, name = 'templates'),
    path('create_template/', create_template, name = 'create_template'),
    
]

