# Generated by Django 5.0.1 on 2024-01-11 05:00

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_sizead_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Введите название')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Информационный текст')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('price_sale', models.FloatField(blank=True, null=True, verbose_name='Цена со скидкой(если есть скидка)')),
            ],
            options={
                'verbose_name': '9) Добавить Одежду для главной страницы ',
                'verbose_name_plural': '9) Добавить Одежду для главной страницы ',
            },
        ),
        migrations.CreateModel(
            name='IndexImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='sale/', verbose_name='Фотографии одежды')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image_index', to='products.indexproduct')),
            ],
            options={
                'verbose_name': 'Добавить Фотографию',
                'verbose_name_plural': 'Добавить Фотографию',
            },
        ),
    ]
