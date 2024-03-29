# Generated by Django 5.0.1 on 2024-01-10 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_twocategory_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_twoo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_category_twoo', to='products.categoryadd', verbose_name='Выберите вторичную категорию в которую входит данный продукт'),
            preserve_default=False,
        ),
    ]
