from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Reminder, Client, ReminderSequence
from .forms import ReminderForm, ClientForm, ReminderSequenceForm
from datetime import date, timedelta
from .forms import ContactForm 
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
    return render(request, 'reminders.html', {'reminders': reminders})


def add_reminder(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        sequence_forms = [ReminderSequenceForm(request.POST, prefix=str(i)) for i in range(len(request.POST.getlist('duration_value')))]
        
        if reminder_form.is_valid() and all([sf.is_valid() for sf in sequence_forms]):
            reminder = reminder_form.save()
            for sequence_form in sequence_forms:
                sequence = sequence_form.save(commit=False)
                sequence.reminder = reminder
                sequence.save()
            return redirect('reminders_list')
    else:
        reminder_form = ReminderForm()
        sequence_forms = [ReminderSequenceForm(prefix='0')]

    return render(request, 'add_reminder.html', {
        'reminder_form': reminder_form,
        'sequence_forms': sequence_forms,
    })

def reminder_detail(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    return render(request, 'reminder_detail.html', {'reminder': reminder})


def reminder_success(request):
    return render(request, 'reminder_success.html')
    

def calendar(request):
    reminders = Reminder.objects.all()
    return render(request, 'calendar.html')

def settings(request):
    return render(request, 'settings.html')

def clients_due(request):
    today = date.today()
    due_soon = Reminder.objects.filter(date__range=[today, today + timedelta(days=7)])
    return render(request, 'clients_due.html', {'due_soon': due_soon})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_details(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_details.html', {'client': client})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})

def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'delete_client.html', {'client': client})

def templates(request):
    return render(request, 'templates.html')

def create_template(request):
    if request.method == 'POST':
        template_name = request.POST.get('templateName')
        template_content = request.POST.get('templateContent')
        
        template = Template.objects.create(
            template_name=template_name,
            template_content=template_content,
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


