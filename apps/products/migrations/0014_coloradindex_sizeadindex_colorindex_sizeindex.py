# Generated by Django 5.0.1 on 2024-01-12 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_indexproduct_brand_indexproduct_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorAdIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Введите цвет ')),
            ],
            options={
                'verbose_name': '6) Добавить Цвет',
                'verbose_name_plural': '6) Добавить Цвета',
            },
        ),
        migrations.CreateModel(
            name='SizeAdIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Укажите Размер в письменном ввиде полностью')),
                ('al', models.CharField(max_length=2, verbose_name='Укажите Размер в письменном ввиде сокращенно ')),
            ],
            options={
                'verbose_name': '7) Добавить Размер',
                'verbose_name_plural': '7) Добавить Размеры',
            },
        ),
        migrations.CreateModel(
            name='ColorIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color_index', to='products.indexproduct')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color_ad_index', to='products.coloradindex')),
            ],
            options={
                'verbose_name': 'Добавить Цвет',
                'verbose_name_plural': 'Добавить Цвета',
            },
        ),
        migrations.CreateModel(
            name='SizeIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size_index', to='products.indexproduct')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size_ad_index', to='products.sizeadindex')),
            ],
            options={
                'verbose_name': 'Добавить Размер',
                'verbose_name_plural': 'Добавить Размеры',
            },
        ),
    ]