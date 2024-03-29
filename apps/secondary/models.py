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
        verbose_name = "1) Слайд"
        verbose_name_plural = "1) Слайды"

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
        verbose_name = "2) Образцы & О нас"
        verbose_name_plural = "2) Образцы & О нас "
    
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

################################################################################################################################################################################

class Banner(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='banner/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    class Meta:
        verbose_name = "3) Баннер & Наши Бренды"
        verbose_name_plural = "3)Баннер & Наши Бренды "
    
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
        verbose_name = " Добавить фото образцов"
        verbose_name_plural = " Добавить фото образцов"

################################################################################################################################################################################
class Faqs(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Вопрос"
    )
    message = RichTextField(
        verbose_name="Информационный текст",
    )
    
    def __str__(self):
        return f"{self.title} - {self.message}"
    
    class Meta:
        verbose_name = "5) Часто задаваемые вопросы"
        verbose_name_plural = "5) Часто задаваемые вопросы "

class Team(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='team/',
        verbose_name="Фотография",
        blank = False, null = False
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Имя"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = "Должность"
    )

    def __str__(self):
        return f"{self.title} - {self.work}"
    
    class Meta:
        verbose_name = "4) Наша комманда"
        verbose_name_plural = "4) Наша комманда "