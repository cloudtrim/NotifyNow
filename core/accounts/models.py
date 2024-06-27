from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accounts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    repeat_interval = models.CharField(max_length=50, choices=[
        ('none', 'None'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('custom', 'Custom')
    ])
    notes = models.TextField(blank=True, null=True)
    notify_email = models.BooleanField(default=False)
    notify_sms = models.BooleanField(default=False)
    notify_push = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
