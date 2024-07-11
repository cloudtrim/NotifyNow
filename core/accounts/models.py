from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accounts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

# class Client(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)


#     def __str__(self):
#         return self.name

class Client(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    service_type = models.CharField(max_length = 50, blank=True, null=True)
    reminders = models.IntegerField(default=0)
    user = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# class Reminder(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    # title = models.CharField(max_length=200)
    # date = models.DateField()
    # time = models.TimeField()
    # repeat_interval = models.CharField(max_length=50, choices=[
    #     ('none', 'None'),
    #     ('daily', 'Daily'),
    #     ('weekly', 'Weekly'),
    #     ('monthly', 'Monthly'),
    #     ('custom', 'Custom')
    # ])
    # notes = models.TextField(blank=True, null=True)
    # notify_email = models.BooleanField(default=False)
    # # notify_sms = models.BooleanField(default=False)
    # notify_push = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.title
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    expiry_date = models.DateField()
    clients = models.ManyToManyField(Client)
    duration = models.IntegerField()  # Store duration as a single integer
    reminder_time = models.TimeField()

    def __str__(self):
        return self.title
    
    


# class CustomField(models.Model):
#     FIELD_TYPE_CHOICES = [
#         ('text', 'Text'),
#         ('numeric', 'Numeric')
#     ]
    
#     contact = models.ForeignKey(Client, related_name='custom_fields', on_delete=models.CASCADE)
#     field_type = models.CharField(max_length=10, choices=FIELD_TYPE_CHOICES)
#     label = models.CharField(max_length=50)
#     value = models.CharField(max_length=100)

#     def __str__(self):
#         return f'{self.label}: {self.value}'
    

class Template(models.Model):
    template_name = models.CharField(max_length=100)
    template_content = models.TextField()
    # user = models.CharField(max_length=100)  # Assuming user is a text field

    def __str__(self):
        return self.template_name