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
    title = models.CharField(max_length=255, default=None)
    content = models.TextField(default=None)

    def __str__(self):
        return self.name
    
class Reminder(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()    
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return self.title

class ReminderSequence(models.Model):
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE, related_name='sequences')
    duration_value = models.PositiveIntegerField()
    duration_unit = models.CharField(max_length=10, choices=[('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months')])
    before_after = models.CharField(max_length=10, choices=[('before', 'Before'), ('after', 'After')])
    reminder_time = models.TimeField()

    def __str__(self):
        return f"Sequence for {self.reminder.name} - {self.duration_value} {self.duration_unit} {self.before_after}"
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title