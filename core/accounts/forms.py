from django import forms
from .models import Reminder, Client, CustomField, Contact

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'date', 'time', 'repeat_interval', 'notes', 'notify_email', 'notify_sms', 'notify_push']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['group', 'first_name', 'last_name', 'email', 'mobile_number']

class CustomFieldForm(forms.ModelForm):
    class Meta:
        model = CustomField
        fields = ['field_type', 'label', 'value']