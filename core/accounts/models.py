from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accounts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)


class Client(models.Model):
    name = models.CharField(max_length=255, default=None)
    email = models.EmailField(unique=True, default=None)
    contact_number = models.CharField(max_length=15)
    service_type = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name
    

class Template(models.Model):
    template_name = models.CharField(max_length=100)
    template_content = models.TextField()
    # user = models.CharField(max_length=100)  # Assuming user is a text field

    def __str__(self):
        return self.template_name


class Reminder(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    due_time = models.TimeField()
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return self.name

class ReminderSequence(models.Model):
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE, related_name='sequences')
    duration_value = models.PositiveIntegerField()
    duration_unit = models.CharField(max_length=10, choices=[('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')])
    before_after = models.CharField(max_length=10, choices=[('before', 'Before'), ('after', 'After')])
    reminder_time = models.TimeField()

    def __str__(self):
        return f"Sequence for {self.reminder.name} - {self.duration_value} {self.duration_unit} {self.before_after}"