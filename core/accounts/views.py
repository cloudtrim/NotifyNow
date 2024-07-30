from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Reminder, Client, ReminderSequence, Event
from .forms import ReminderForm, ClientForm, ReminderSequenceForm, EventForm
from django.http import JsonResponse
from datetime import date, timedelta
from django.forms import modelformset_factory
from django.views.decorators.http import require_POST
from .models import Template
from .forms import TemplateForm
from django.core.mail import send_mail
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm, CustomPasswordChangeForm




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


def reminder_detail(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    sequences = reminder.sequences.all()
    return render(request, 'reminder_detail.html', {'reminder': reminder, 'sequences': sequences})



def add_reminder(request):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        #logger.info(reminder_form)
        sequence_forms = [ReminderSequenceForm(request.POST, prefix=str(i)) for i in range(len(request.POST.getlist('duration_value')))]
        logger.info(sequence_forms)
        if reminder_form.is_valid():
            logger.info("reminder_form.is_valid")
        
        
        if reminder_form.is_valid() and all([sf.is_valid() for sf in sequence_forms]):
            reminder = reminder_form.save(commit=False)
            reminder.save()
            reminder_form.save_m2m() 
            logger.info("form is valid now saving")
            for sequence_form in sequence_forms:
                sequence = sequence_form.save(commit=False)
                sequence.reminder = reminder
                sequence.save()
            return redirect('reminders_list')
        else :
            logger.info("nothing to save")
    else:
        reminder_form = ReminderForm()
        sequence_forms = [ReminderSequenceForm(prefix='0')]

    return render(request, 'add_reminder.html', {
        'reminder_form': reminder_form,
        'sequence_forms': sequence_forms,
    })



def edit_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST, instance=reminder)
        sequence_forms = [ReminderSequenceForm(request.POST, prefix=str(i)) for i in range(len(request.POST.getlist('duration_value')))]
        
        if reminder_form.is_valid() and all([sf.is_valid() for sf in sequence_forms]):
            reminder = reminder_form.save()
            
            reminder.sequences.all().delete()  # Remove old sequences
            for sequence_form in sequence_forms:
                sequence = sequence_form.save(commit=False)
                sequence.reminder = reminder
                sequence.save()
            return redirect('reminders_list')
    else:
        reminder_form = ReminderForm(instance=reminder)
        sequence_forms = [ReminderSequenceForm(prefix=str(i), instance=sequence) for i, sequence in enumerate(reminder.sequences.all())]

    return render(request, 'add_reminder.html', {
        'reminder_form': reminder_form,
        'sequence_forms': sequence_forms,
    })

def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    reminder.delete()
    return redirect('reminders_list')

def reminder_detail(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    return render(request, 'reminder_detail.html', {'reminder': reminder})


def reminder_success(request):
    return render(request, 'reminder_success.html')
    

def calendar(request):
    reminders = Reminder.objects.all()
    events = Event.objects.all()
    logger.info("got events = {}".format(events))
    return render(request, 'calendar.html', {'events': events})

def settings(request):
    return render(request, 'settings.html')


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
    templates = Template.objects.all()
    return render(request, 'templates.html', {'templates': templates})

def template_details(request, pk):
    template = get_object_or_404(Template, pk=pk)
    return render(request, 'client_details.html', {'template': template})

def create_template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templates')
    else:
        form = TemplateForm()
    return render(request, 'create_template.html', {'form': form})

def update_template(request, pk):
    template = get_object_or_404(Template, pk=pk)
    if request.method == 'POST':
        form = TemplateForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
            return redirect('templates')
    else:
        form = TemplateForm(instance=template)
    return render(request, 'update_template.html', {'form': form})

def delete_template(request, pk):
    template = get_object_or_404(Template, pk=pk)
    if request.method == 'POST':
        template.delete()
        return redirect('templates')
    return render(request, 'delete_template.html', {'template': template})



def fill_template(template, client_name, due_date, service_type):
    filled_template = template.matter
    filled_template = filled_template.replace("{client_name}", client_name)
    filled_template = filled_template.replace("{due_date}", due_date)
    filled_template = filled_template.replace("{service_type}", service_type)
    return filled_template
    

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


def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        logger.info("got form to save :{}".format(form))
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_data(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
            'id': event.id 
        })
    return JsonResponse(event_list, safe=False)

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})



@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  
            return redirect('profile')
    else:
        password_form = CustomPasswordChangeForm(user)
    
    profile_form = ProfileForm(instance=user)
    return render(request, 'profile.html', {'profile_form': profile_form, 'password_form': password_form})


def reminders_list(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder_list.html', {'reminders': reminders})