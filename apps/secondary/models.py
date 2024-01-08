from django.db import models
from django.core.exceptions import ValidationError
from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField
# Create your models here.
class Slide(models.Model):
    subtitle = models.CharField(
        max_length = 200,
        verbose_name = "Введите подзаголовок"
    )
    title  = models.CharField(
        max_length = 200,
        verbose_name = "Введите заголовок"
    )
    descriptions = models.CharField(
        max_length = 200,
        verbose_name = "Введите заголовок"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    def __str__(self):
        return f"{self.subtitle} - {self.title}"
    
    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

################################################################################################################################################################################

class LookBook(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
    )
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Образцы & О нас"
        verbose_name_plural = "Образцы & О нас "
    
class LookBookAdd(models.Model):
    settings = models.ForeignKey(LookBook, related_name='look_book', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
        verbose_name="Фотография",
        blank = False, null = False
    )

    class Meta:
        verbose_name = "Добавить фото образцов"
        verbose_name_plural = "Добавить фото образцов"

class Banner(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='banner/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    class Meta:
        verbose_name = "Баннер & Наши Бренды"
        verbose_name_plural = "Баннер & Наши Бренды "
    
class BannerAdd(models.Model):
    settings = models.ForeignKey(Banner, related_name='banner_add', on_delete=models.CASCADE)
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='brand/',
        verbose_name="Фотография",
        blank = False, null = False
    )

    class Meta:
        verbose_name = "Добавить фото образцов"
        verbose_name_plural = "Добавить фото образцов"