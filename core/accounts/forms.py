from django import forms
from .models import Reminder, Client, Template, ReminderSequence



class ClientSelectionForm(forms.Form):
    clients = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.SelectMultiple)

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'due_date', 'due_time', 'clients']
        widgets = {
            'clients': forms.CheckboxSelectMultiple(),
        }

class ReminderSequenceForm(forms.ModelForm):
    class Meta:
        model = ReminderSequence
        fields = ['duration_value', 'duration_unit', 'before_after', 'reminder_time']
        widgets = {
            'duration_unit': forms.Select(choices=[('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')]),
            'before_after': forms.Select(choices=[('before', 'Before'), ('after', 'After')]),
        }
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'contact_number', 'service_type']

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['title', 'content']