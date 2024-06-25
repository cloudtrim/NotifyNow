from django.shortcuts import render, redirect
from .models import Reminder
from .forms import ReminderForm

def reminders(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/reminders.html')

def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminders')
    else:
        form = ReminderForm()
    return render(request, 'reminders/add_reminder.html')

def calendar(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminders/calendar.html')

def settings(request):
    return render(request, 'reminders/settings.html')
