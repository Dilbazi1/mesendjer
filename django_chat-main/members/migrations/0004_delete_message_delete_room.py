# Generated by Django 4.2.3 on 2023-12-18 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_remove_message_is_staff_members_is_staff"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
        migrations.DeleteModel(
            name="Room",
        ),
    ]
