# Generated by Django 5.0 on 2024-01-04 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]