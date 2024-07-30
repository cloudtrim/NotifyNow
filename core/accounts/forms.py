from django import forms
from .models import Reminder, Client, Template, ReminderSequence, Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm




class ClientSelectionForm(forms.Form):
    clients = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.SelectMultiple)

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'due_date', 'clients']
        widgets = {            
           'due_date' : forms.DateTimeInput(attrs={'type': 'datetime-local'})           
        }

class ReminderSequenceForm(forms.ModelForm):
    class Meta:
        model = ReminderSequence
        fields = ['duration_value', 'duration_unit', 'before_after', 'reminder_time']
        widgets = {
            'duration_unit': forms.Select(choices=[('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')]),
            'before_after': forms.Select(choices=[('before', 'Before'), ('after', 'After')]),
            'reminder_time' : forms.TimeInput(attrs={'type': 'time'})
        }
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'contact_number', 'service_type']

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['title', 'content']



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = "Old Password"
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm New Password"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }