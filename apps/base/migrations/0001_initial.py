# Generated by Django 5.0.1 on 2024-01-07 22:09

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Информационный текст')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип Компании')),
                ('logo_complex', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип Комплекса')),
                ('email', models.EmailField(max_length=255, verbose_name='Почта')),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatspp URL')),
                ('whatsapp_number', models.CharField(max_length=255, verbose_name='Whatsapp номер')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram URL')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Youtube URL')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook URL')),
            ],
            options={
                'verbose_name': 'Основная настройка',
                'verbose_name_plural': 'Основные настройки',
            },
        ),
        migrations.CreateModel(
            name='SettingsPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_title', to='base.settings')),
            ],
            options={
                'verbose_name': 'Дополнительный телефонный номер',
                'verbose_name_plural': 'Дополнительный телефонный номер',
                'unique_together': {('settings', 'phone')},
            },
        ),
    ]
