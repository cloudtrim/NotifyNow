from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Reminder, Client
from .forms import ReminderForm, ClientForm
from datetime import date, timedelta


# Create your views here.
def home(request):
    return render(request, "home.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid username.')
            return redirect('/login_page')

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, 'Invalid password.')
            print("invalid password")
            return redirect('/login_page')
        else:
            login(request, user)
            return redirect('/dashboard')

    return render(request, "login_page.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already exists.')
            return redirect('/signup/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully.')

        return redirect('/signup/')



    return render(request, "signup.html")

def dashboard(request):
    return render(request, "dashboard.html")

def reminders(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders.html')

def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminders')
    else:
        form = ReminderForm()
    return render(request, 'add_reminder.html')

def calendar(request):
    reminders = Reminder.objects.all()
    return render(request, 'calendar.html')

def settings(request):
    return render(request, 'settings.html')

def clients_due(request):
    today = date.today()
    due_soon = Reminder.objects.filter(date__range=[today, today + timedelta(days=7)])
    return render(request, 'clients_due.html', {'due_soon': due_soon})