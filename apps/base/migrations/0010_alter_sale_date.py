# Generated by Django 5.0.1 on 2024-01-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(verbose_name='Время окончания'),
        ),
    ]
