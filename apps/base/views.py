from django.shortcuts import render,redirect
from datetime import datetime

################################################################################################################################################################################

from apps.base import models
from apps.secondary.models import Slide,LookBook,Banner
from apps.contacts.models import Review,Subscriber,Buy
from apps.products.models import Category,Product, IndexProduct,Collection
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
#FILTER_____________________________________________
    collection = Collection.objects.all()
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    category = Category.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.all().order_by("?")[:3]

    product = Product.objects.all().order_by("?")[:10]
    products_id = IndexProduct.objects.latest("id")

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
    lookbook = LookBook.objects.latest("id")
    slide = Slide.objects.all()
    banner = Banner.objects.latest("id")

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
        if "submit_application" in request.POST:
            product = products_id.title
            color = request.POST.get("color")
            size = request.POST.get("size")
            username = request.POST.get("username")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            buy = Buy.objects.create(product=product,color=color,size=size,username=username,phone=phone,email=email)
            get_text(f"""
                ✅Пользователь оставил заявку на покупку
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Название товара: {product}
Цвет товара: {color}
Размер товара: {size}
ФИО клиента: {username}
Телефонный номер клиента: {phone}
Почта клиента: {email}
""")
            return redirect( 'index')
    reviews = Review.objects.all()
    return render(request,'base/index-2.html', locals())

################################################################################################################################################################################

def blog(request):
#Base----------------------------------------------------------
    collection = Collection.objects.all()
    settings = models.Settings.objects.latest("id")
    category = Category.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.all().order_by("?")
    #################################################
    sales = models.Sale.objects.first()

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
            subscribe = Subscriber.objects.create(email = email)
            get_text(f"""
                ✅Пользователь подписался на рассылку
                         
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                         
Почта пользователя: {email}
""")
            return redirect( 'index')
    return render(request,'secondary/single-article.html', locals())

def blog_detail(request,id):
    collection = Collection.objects.all()
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    category = Category.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.get(id=id)
    blog_all = models.Blog.objects.all().order_by("?")

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
    return render(request,'secondary/blog-single.html', locals())