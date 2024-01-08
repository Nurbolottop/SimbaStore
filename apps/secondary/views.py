from django.shortcuts import render,redirect
from datetime import datetime

################################################################################################################################################################################

from apps.base import models
from apps.secondary.models import Faqs,Team
from apps.contacts.models import Review,Subscriber
from apps.telegram_bot.views import get_text

# Create your views here.
def about(request):
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    category = models.Category.objects.latest("id")
    deviz = models.Devis.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.all().order_by("?")[:3]


    #################################################
    sales = models.Sale.objects.first()

    # Проверяем, что объект существует и имеет установленное время окончания
    if sales and sales.end_date:
        end_time = sales.end_date
    else:
        # Если объект голосования не найден, можно установить временное значение
        # или обработать эту ситуацию как ошибку
        end_time = datetime.now()  # Это просто пример
    context = {'end_time': end_time.isoformat()}
    # Передаем в шаблон строку в формате ISO
    context = {'end_time': end_time.isoformat()}

#Secondary----------------------------------------------------------
    team = Team.objects.all()

#Contacts ----------------------------------------------------------
    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            subscribe = Subscriber.objects.create(email = email)
            get_text(f"""
                ✅Пользователь подписался на рассылку
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Почта пользователя: {email}
""")
            return redirect( 'index')
    reviews = Review.objects.all()
    return render(request,'base/about.html', locals())

################################################################################################################################################################################

def faqs(request):
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    category = models.Category.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.all().order_by("?")[:3]


    #################################################
    sales = models.Sale.objects.first()

    # Проверяем, что объект существует и имеет установленное время окончания
    if sales and sales.end_date:
        end_time = sales.end_date
    else:
        # Если объект голосования не найден, можно установить временное значение
        # или обработать эту ситуацию как ошибку
        end_time = datetime.now()  # Это просто пример
    context = {'end_time': end_time.isoformat()}
    # Передаем в шаблон строку в формате ISO
    context = {'end_time': end_time.isoformat()}

#Secondary----------------------------------------------------------
    faqs = Faqs.objects.all()
#Contacts ----------------------------------------------------------
    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            subscribe = Subscriber.objects.create(email = email)
            get_text(f"""
                ✅Пользователь подписался на рассылку
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Почта пользователя: {email}
""")
            return redirect( 'index')
    reviews = Review.objects.all()
    return render(request,'secondary/faqs.html', locals())

################################################################################################################################################################################
