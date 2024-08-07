# Generated by Django 4.2.9 on 2024-07-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0017_remove_reminder_date_remove_reminder_notes_and_more"),
    ]

    operations = [
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
            name="template",
        ),
        migrations.RemoveField(
            model_name="reminder",
            name="time",
        ),
        migrations.AddField(
            model_name="reminder",
            name="count",
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name="reminder",
            name="notification_time",
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name="reminder",
            name="notify_before_after",
            field=models.CharField(
                choices=[("before", "Before"), ("after", "After")],
                default=None,
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="reminder",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
