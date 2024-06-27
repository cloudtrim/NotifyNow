from django import forms
from .models import Reminder, Client

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'date', 'time', 'repeat_interval', 'notes', 'notify_email', 'notify_sms', 'notify_push']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']