# Generated by Django 4.2.14 on 2024-10-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acm_website", "0007_alter_user_badges_alter_user_events_attended"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="hide",
            field=models.BooleanField(default=False, help_text="Hide this user"),
        ),
    ]