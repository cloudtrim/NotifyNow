from django import forms
from .models import Reminder, Client, Template
from .widgets import MultiSelectWithCheckboxes

# class ReminderForm(forms.ModelForm):
#     class Meta:
#         model = Reminder
#         # fields = ['title', 'date', 'time', 'repeat_interval', 'notes', 'notify_email', 'notify_push']
#         fields = ['title', 'expiration_date', 'clients', 'duration_value', 'duration_unit', 'before_after', 'notification_time']
#         widgets = {
#             'clients': forms.CheckboxSelectMultiple,
#         }
class ReminderForm(forms.ModelForm):
    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(), 
        widget=MultiSelectWithCheckboxes()
    )
    
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    reminder_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    DURATION_CHOICES = [
        (1, '1 day before'),
        (2, '2 days before'),
        (7, '1 week before'),
        (30, '1 month before'),
        (-1, '1 day after'),
        (-2, '2 days after'),
        (-7, '1 week after'),
        (-30, '1 month after')
    ]
    duration = forms.ChoiceField(choices=DURATION_CHOICES)

    class Meta:
        model = Reminder
        fields = ['title', 'expiry_date', 'clients', 'duration', 'reminder_time']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = ['name', 'email', 'contact_number']
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'service_type']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'service_type']

# class CustomFieldForm(forms.ModelForm):
#     class Meta:
#         model = CustomField
#         fields = ['field_type', 'label', 'value']

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['template_name', 'template_content']