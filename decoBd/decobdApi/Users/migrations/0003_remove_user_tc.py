# Generated by Django 4.0.3 on 2024-03-19 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_name_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tc',
        ),
    ]