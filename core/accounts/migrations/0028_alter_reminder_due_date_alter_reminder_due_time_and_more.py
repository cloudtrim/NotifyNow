# Generated by Django 4.2.9 on 2024-07-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0027_remove_client_reminders_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reminder",
            name="due_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="reminder",
            name="due_time",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="remindersequence",
            name="reminder_time",
            field=models.DateTimeField(),
        ),
    ]
