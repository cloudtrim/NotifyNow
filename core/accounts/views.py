from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
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
from django.views.decorators.http import require_POST
from .models import Template
from .forms import TemplateForm
from django.core.mail import send_mail
import logging
logger = logging.getLogger('notfyNowApp')

# Create your views here.
def home(request):
    return render(request, "home.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
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
        logger.debug(" reminder_title :{}, expiration_date :{} ".format(reminder_title,expiration_date))
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
        logger.debug("contact_form = {}".format(contact_form))
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
    if request.method == 'POST':
        template_name = request.POST.get('templateName')
        template_content = request.POST.get('templateContent')
        user = request.POST.get('user')
        
        template = Template.objects.create(
            template_name=template_name,
            template_content=template_content,
            user=user
        )
        
        return redirect('/input_details/')  
    else:
        return render(request, 'create_template.html')
    

def input_details(request):
    templates = Template.objects.all()  
    return render(request, 'input_details.html', {'templates': templates})

def send_template(request):
    if request.method == 'POST':
        template_id = request.POST.get('template')
        template = get_object_or_404(Template, id=template_id)
        
        title = request.POST.get('title')
        client_name = request.POST.get('clientName')
        date = request.POST.get('date')
        email = request.POST.get('email')
        
        template_content = template.template_content
        template_content = template_content.replace('[TITLE]', title)
        template_content = template_content.replace('[CLIENT_NAME]', client_name)
        template_content = template_content.replace('[DATE]', date)
        
        send_mail(
            subject=template.template_name,
            message=template_content,
            from_email='antharev@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
        
        return redirect('/success/') 
    else:
        return redirect('/input_details/')
    

def success(request):
    return render(request, 'success.html')


