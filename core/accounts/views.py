from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Reminder, Client
from .forms import ReminderForm, ClientForm
from datetime import date, timedelta
from .models import Contact, CustomField
from .forms import ContactForm, CustomFieldForm
from django.forms import modelformset_factory


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
        reminder_title = request.POST.get('reminder_title')
        expiration_date = request.POST.get('expiration_date')
        notes = request.POST.get('notes')
        durations = request.POST.getlist('duration[]')
        duration_types = request.POST.getlist('duration_type[]')
        duration_relatives = request.POST.getlist('duration_relative[]')
        times = request.POST.getlist('time[]')
        email_templates = request.POST.getlist('email_template[]')
        sms_templates = request.POST.getlist('sms_template[]')
        auto_renew = request.POST.get('auto_renew') == 'on'
        every = request.POST.get('every')
        every_unit = request.POST.get('every_unit')
        ends = request.POST.get('ends')
        renewals = request.POST.get('renewals')
        renew_type = request.POST.get('renew_type')
        renew_update = request.POST.get('renew_update') == 'on'
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


def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts_list.html', {'contacts': contacts})


def create_contact(request):
    CustomFieldFormSet = modelformset_factory(CustomField, form=CustomFieldForm, extra=1, can_delete=True)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        formset = CustomFieldFormSet(request.POST, queryset=CustomField.objects.none())
        
        if contact_form.is_valid() and formset.is_valid():
            contact = contact_form.save()
            for form in formset:
                if form.cleaned_data:
                    custom_field = form.save(commit=False)
                    custom_field.contact = contact
                    custom_field.save()
            return redirect('contacts_list')
    else:
        contact_form = ContactForm()
        formset = CustomFieldFormSet(queryset=CustomField.objects.none())
    
    return render(request, 'create_contact.html', {
        'contact_form': contact_form,
        'formset': formset
    })

def templates(request):
    return render(request, 'templates.html')

def create_template(request):
    return render(request, 'create_template.html')