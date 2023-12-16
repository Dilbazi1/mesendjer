# Generated by Django 4.2.3 on 2023-12-15 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("chat", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="chat.group"
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
