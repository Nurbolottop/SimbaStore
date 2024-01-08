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
    class Meta:
        verbose_name = "Добавить категории"
        verbose_name_plural = "Добавить категории"

################################################################################################################################################################################
