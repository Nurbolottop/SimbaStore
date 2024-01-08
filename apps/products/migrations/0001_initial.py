# Generated by Django 5.0.1 on 2024-01-08 12:38

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Информационный текст')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CategoryAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='6', max_length=255, verbose_name='Нумерация')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='category/', verbose_name='Фотография')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorys', to='products.category')),
            ],
            options={
                'verbose_name': 'Добавить категории',
                'verbose_name_plural': 'Добавить категории',
            },
        ),
    ]
