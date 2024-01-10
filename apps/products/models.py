from django.db import models

from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 
# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Заголовок"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
    )
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "1) Категория"
        verbose_name_plural = "1) Категории"

class CategoryAdd(models.Model):
    settings = models.ForeignKey(Category,related_name = "categorys", on_delete = models.CASCADE)
    number = models.CharField(
        max_length = 255,
        default = '6',
        verbose_name = "Нумерация"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name  = "Название категории"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='category/',
        verbose_name="Фотография",
        blank = False, null = False
    )
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Добавить категории"
        verbose_name_plural = "Добавить категории"

################################################################################################################################################################################

class TwoCategory(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название под категории"
    )
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "2) Добавить Вторичную Категорию"
        verbose_name_plural = "2) Добавить Вторичную Категорию"

class Brand(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название бренда"
    )
    def __str__(self):
        return f"{self.title} "
    
    class Meta:
        verbose_name = "3) Добавить Бренд"
        verbose_name_plural = "3) Добавить Бренды"

################################################################################################################################################################################

class Collection (models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название коллекции"
    )
    def __str__(self):
        return f"{self.title} "
    
    class Meta:
        verbose_name = "4) Добавить Коллекцию"
        verbose_name_plural = "4) Добавить Коллекции"

################################################################################################################################################################################

class Price(models.Model):
    title = models.FloatField(
        verbose_name = "цена"
    )
    def __str__(self):
        return f"{self.title} "
    
    class Meta:
        verbose_name = "5) Добавить Цены"
        verbose_name_plural = "5) Добавить Цены"

################################################################################################################################################################################

class Product(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Введите название"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='sale/',
        verbose_name="Банерная фотография",
        blank = False, null = False
    )
    price = models.FloatField(
        verbose_name = "Цена"
    )
    price_sale = models.FloatField(
        blank = True,null = True,
        verbose_name = "Цена со скидкой(если есть скидка)"
    )
    category  = models.ForeignKey(CategoryAdd, 
        related_name = "product_category",
        on_delete = models.CASCADE,
        verbose_name = "Выберите категорию в которую входит данный продукт"
    )
    category_twoo  = models.ForeignKey(TwoCategory, 
        related_name = "product_category_twoo",
        on_delete = models.CASCADE,
        verbose_name = "Выберите вторичную категорию в которую входит данный продукт"
    )
    brand  = models.ForeignKey(Brand, 
        related_name = "product_brand",
        on_delete = models.CASCADE,
        verbose_name = "Выберите бренд в которую входит данный продукт"

    )
    collection  = models.ForeignKey(Collection, 
        related_name = "product_collection",
        on_delete = models.CASCADE,
        verbose_name = "Выберите коллекцию в которую входит данный продукт"

    )
    prices  = models.ForeignKey(Price, 
        related_name = "product_prices",
        on_delete = models.CASCADE,
        verbose_name = "Выберите цену в которую входит данный продукт"

    )

    def __str__(self):
        return f"{self.title}  - {self.price}"
    
    class Meta:
        verbose_name = "8) Добавить Одежду"
        verbose_name_plural = "8) Добавить Одежду"



class Image(models.Model):
    settings = models.ForeignKey(Product,
        related_name = "product_image",
        on_delete = models.CASCADE
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='sale/',
        verbose_name="Фотографии одежды",
        blank = False, null = False
    )
    class Meta:
        verbose_name = "Добавить Фотографию"
        verbose_name_plural = "Добавить Фотографию"

################################################################################################################################################################################

class ColorAd(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Введите цвет "
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "6) Добавить Цвет"
        verbose_name_plural = "6) Добавить Цвета"

class Color(models.Model):
    settings = models.ForeignKey(ColorAd,
        related_name = "product_color",
        on_delete = models.CASCADE
    )
    title = models.ForeignKey(Product,
        related_name = "product_color_ad",
        on_delete = models.CASCADE
    )

    def __str__(self):
        return f"{self.title} "
    
    class Meta:
        verbose_name = "Добавить Цвет"
        verbose_name_plural = "Добавить Цвета"
################################################################################################################################################################################

class SizeAd(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Укажите Размер в письменном ввиде полностью",
        blank=True,null = True
    )
    al = models.CharField(
        max_length  = 2,
        verbose_name = "Укажите Размер в письменном ввиде сокращенно "
    )
    def __str__(self):
        return f"{self.title} - {self.al}"
    
    class Meta:
        verbose_name = "7) Добавить Размер"
        verbose_name_plural = "7) Добавить Размеры"

class Size(models.Model):
    settings = models.ForeignKey(Product,
        related_name = "product_size",
        on_delete = models.CASCADE
    )
    title = models.ForeignKey(SizeAd,
        related_name = "product_size_ad",
        on_delete = models.CASCADE
    )
    def __str__(self):
        return f"{self.title} "
    
    class Meta:
        verbose_name = "Добавить Размер"
        verbose_name_plural = "Добавить Размеры"