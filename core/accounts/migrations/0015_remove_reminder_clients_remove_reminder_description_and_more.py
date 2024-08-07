# Generated by Django 4.2.9 on 2024-07-13 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0014_rename_reminder_time_reminder_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reminder",
            name="clients",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="description",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="duration",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="duration_type",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="expiry_date",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="template",
        ),
        migrations.AddField(
            model_name="reminder",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.client",
            ),
        ),
        migrations.AddField(
            model_name="reminder",
            name="date",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="reminder",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reminder",
            name="notify_email",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="reminder",
            name="notify_push",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="reminder",
            name="notify_sms",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="reminder",
            name="repeat_interval",
            field=models.CharField(
                choices=[
                    ("none", "None"),
                    ("daily", "Daily"),
                    ("weekly", "Weekly"),
                    ("monthly", "Monthly"),
                    ("custom", "Custom"),
                ],
                default=None,
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="reminder",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="reminder",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
