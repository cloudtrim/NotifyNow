# Generated by Django 4.2.9 on 2024-07-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0020_remove_reminder_notes_remove_reminder_notify_email_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reminder",
            name="client",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="date",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="time",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="title",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="user",
        ),
        migrations.RemoveField(
            model_name="remindersequence",
            name="sequence_date",
        ),
        migrations.RemoveField(
            model_name="remindersequence",
            name="sequence_name",
        ),
        migrations.RemoveField(
            model_name="remindersequence",
            name="sequence_time",
        ),
        migrations.AddField(
            model_name="reminder",
            name="clients",
            field=models.ManyToManyField(to="accounts.client"),
        ),
        migrations.AddField(
            model_name="reminder",
            name="due_date",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="reminder",
            name="due_time",
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name="reminder",
            name="name",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="remindersequence",
            name="before_after",
            field=models.CharField(
                choices=[("before", "Before"), ("after", "After")],
                default=None,
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="remindersequence",
            name="duration_unit",
            field=models.CharField(
                choices=[("days", "Days"), ("weeks", "Weeks"), ("months", "Months")],
                default=None,
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="remindersequence",
            name="duration_value",
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name="remindersequence",
            name="reminder_time",
            field=models.TimeField(default=None),
        ),
    ]