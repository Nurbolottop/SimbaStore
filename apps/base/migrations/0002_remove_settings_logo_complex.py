# Generated by Django 5.0.1 on 2024-01-08 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='logo_complex',
        ),
    ]