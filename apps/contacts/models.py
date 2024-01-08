from django.db import models
from django.core.mail import EmailMessage
from ckeditor.fields import RichTextField

# Create your models here.

class Review(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    message = models.TextField(
        verbose_name = "Сообщение"
    )
    def __str__(self):
        return f"{self.title} - {self.message}"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

################################################################################################################################################################################

class Subscriber(models.Model):
    email = models.EmailField(
        verbose_name = "Почта пользователя"
    )
    subscribed_at = models.DateTimeField(auto_now_add=True,verbose_name = "Дата подписки") 
    def __str__(self):
        return f"{self.email} - {self.subscribed_at}"
    
    class Meta:
        verbose_name = "Пользователи для рассылки"
        verbose_name_plural = "Пользователи для рассылки"

class Newsletter(models.Model):
    subject = models.CharField(max_length=200, verbose_name="Заголовок")
    message = RichTextField(verbose_name="Сообщение")
    image = models.ImageField(upload_to='newsletter_images/', blank=True, null=True, verbose_name="Изображение")
    attachment = models.FileField(upload_to='newsletter_attachments/', blank=True, null=True, verbose_name="Вложение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Вызываем оригинальный метод save
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            email = EmailMessage(
                self.subject,
                self.message,
                'from@example.com',
                [subscriber.email]
            )
            # Прикрепляем изображение, если оно есть
            if self.image:
                email.attach(self.image.name, self.image.read(), 'image/jpeg')
            
            # Прикрепляем другое вложение, если оно есть
            if self.attachment:
                email.attach(self.attachment.name, self.attachment.read(), self.attachment.file.content_type)
            
            email.send(fail_silently=False)

    class Meta:
        verbose_name = "Отправить рассылку"
        verbose_name_plural = "Отправить рассылку"

################################################################################################################################################################################
