# Generated by Django 4.2.11 on 2024-03-27 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='received_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Message received at'),
            preserve_default=False,
        ),
    ]