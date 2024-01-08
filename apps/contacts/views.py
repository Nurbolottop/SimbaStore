from django.shortcuts import render,redirect
from datetime import datetime
from django.core.mail import send_mail

################################################################################################################################################################################

from apps.contacts import models
from apps.base.models import Settings,Category,Sale
from apps.telegram_bot.views import get_text
# Create your views here.
def reviews(request):
#Base----------------------------------------------------------
    settings = Settings.objects.latest("id")
    category = Category.objects.latest("id")

#Secondary----------------------------------------------------------
    
#Contacts ----------------------------------------------------------
    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            subscribe = models.Subscriber.objects.create(email = email)
            get_text(f"""
                ✅Пользователь подписался на рассылку
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Почта пользователя: {email}
""")
            return redirect( 'index')
        if "reviews" in request.POST:
            title = request.POST.get('title')
            message = request.POST.get('message')
            review = models.Review.objects.create(title = title,message=message)
            get_text(f"""
                ✅Пользователь оставил отзыв!!!
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Имя пользователя: {title}
Отзыв: {message}

""")
            return redirect( 'index')
        
    return render(request,'secondary/reviews.html', locals())


def contact(request):
#Base----------------------------------------------------------
    settings = Settings.objects.latest("id")
    category = Category.objects.latest("id")
    sale = Sale.objects.all()
    #################################################
    sales = Sale.objects.first()

    if sales and sales.end_date:
        end_time = sales.end_date
    else:
        end_time = datetime.now()  # Это просто пример
    context = {'end_time': end_time.isoformat()}

#Secondary----------------------------------------------------------

#Contacts ----------------------------------------------------------
    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            subscriber = models.Subscriber.objects.create(email = email)
            return redirect( 'index')
        if "contaact" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            phone = request.POST.get('phone')
            contacts =models.Contact.objects.create(name = name,email = email,message = message,phone=phone)
            send_mail(
                f'{message}',
                f'Добрый день {name}, спасибо за обратную связь, мы скоро свами свяжемся.Ваше обращение: {message}. Ваша  почта: {email}',
                "noreply@somehost.local",
                [email])
            get_text(f""" ✅Оставлено Заявка на сообщение
                 
                 
ФИО: {contacts.name}
Почта: {contacts.email}
Сообщение: {contacts.message}
Телефонный номер: {contacts.phone}
""")
    return render(request,'base/contact.html', locals())