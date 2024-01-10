from django.shortcuts import render,redirect
from datetime import datetime
from django.core.paginator import Paginator
################################################################################################################################################################################

from apps.base import models
from apps.contacts.models import Review,Subscriber
from apps.secondary.models import Team
from apps.products.models import Category,Product,Brand,ColorAd,SizeAd
from apps.telegram_bot.views import get_text

# Create your views here.
def shop(request):
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    category = Category.objects.latest("id")
    deviz = models.Devis.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.all().order_by("?")[:3]


    #################################################
    sales = models.Sale.objects.first()

    if sales and sales.end_date:
        end_time = sales.end_date
    else:
        end_time = datetime.now()  # Это просто пример
    context = {'end_time': end_time.isoformat()}
    # Передаем в шаблон строку в формате ISO
    context = {'end_time': end_time.isoformat()}

#Secondary----------------------------------------------------------
    
    # Получение параметров фильтрации из запроса
    brand_filter = request.GET.get('brand')
    color_filter = request.GET.get('color')
    size_filter = request.GET.get('size')
    price_filter = request.GET.get('price')
    sort_by = request.GET.get('sort_by', 'featured')

    products = Product.objects.all()

    # Применение фильтров
    if brand_filter:
        products = products.filter(brand__title=brand_filter)
    if color_filter:
        products = products.filter(colorad__title=color_filter)
    if size_filter:
        products = products.filter(sizead__al=size_filter)
    if price_filter:
        products = products.filter(price__lte=price_filter)

    # Сортировка
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    # Добавьте другие условия сортировки по необходимости

    # Получение данных для выпадающих списков фильтров
    brands = Brand.objects.all()
    colors = ColorAd.objects.all()
    sizes = SizeAd.objects.all()

     # Настройка пагинации
    paginator = Paginator(products, 20)  # Показывать 10 продуктов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

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
    return render(request,'shop/shop-category.html', locals())


def shop_detail(request,id):
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    category = Category.objects.latest("id")
    deviz = models.Devis.objects.latest("id")
    sale = models.Sale.objects.all()
    blog = models.Blog.objects.all().order_by("?")[:3]


    #################################################
    sales = models.Sale.objects.first()

    if sales and sales.end_date:
        end_time = sales.end_date
    else:
        end_time = datetime.now()  # Это просто пример
    context = {'end_time': end_time.isoformat()}
    # Передаем в шаблон строку в формате ISO
    context = {'end_time': end_time.isoformat()}

#Secondary----------------------------------------------------------
    products = Product.objects.get(id=id)
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
    return render(request,'shop/shop-single.html', locals())