# Generated by Django 5.0.1 on 2024-01-08 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0007_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '3) Баннер & Наши Бренды', 'verbose_name_plural': '3)Баннер & Наши Бренды '},
        ),
        migrations.AlterModelOptions(
            name='banneradd',
            options={'verbose_name': ' Добавить фото образцов', 'verbose_name_plural': ' Добавить фото образцов'},
        ),
        migrations.AlterModelOptions(
            name='faqs',
            options={'verbose_name': '5) Часто задаваемые вопросы', 'verbose_name_plural': '5) Часто задаваемые вопросы '},
        ),
        migrations.AlterModelOptions(
            name='lookbook',
            options={'verbose_name': '2) Образцы & О нас', 'verbose_name_plural': '2) Образцы & О нас '},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': '1) Слайд', 'verbose_name_plural': '1) Слайды'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': '4) Наша комманда', 'verbose_name_plural': '4) Наша комманда '},
        ),
    ]
