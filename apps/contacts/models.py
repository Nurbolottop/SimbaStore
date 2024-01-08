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
        verbose_name = "4) Отзыв"
        verbose_name_plural = "4) Отзывы"

################################################################################################################################################################################

class Subscriber(models.Model):
    email = models.EmailField(
        verbose_name = "Почта пользователя"
    )
    subscribed_at = models.DateTimeField(auto_now_add=True,verbose_name = "Дата подписки") 
    def __str__(self):
        return f"{self.email} - {self.subscribed_at}"
    
    class Meta:
        verbose_name = "2) Пользователи для рассылки"
        verbose_name_plural = "2) Пользователи для рассылки"

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
        verbose_name = "1) Отправить рассылку"
        verbose_name_plural = "1) Отправить рассылку"

################################################################################################################################################################################

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "3) Запросы на связи"
        verbose_name_plural = "3) Запросы на связь"

################################################################################################################################################################################
