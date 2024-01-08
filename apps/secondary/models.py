from django.db import models
from django_resized.forms import ResizedImageField 
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
