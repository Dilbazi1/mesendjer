# Generated by Django 4.2.3 on 2023-12-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_room_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="is_staff",
        ),
        migrations.AddField(
            model_name="members",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
