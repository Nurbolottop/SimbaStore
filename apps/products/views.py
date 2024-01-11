from django.shortcuts import render,redirect
from datetime import datetime
from django.core.paginator import Paginator
################################################################################################################################################################################

from apps.base import models
from apps.contacts.models import Review,Subscriber
from apps.secondary.models import Team
from apps.products.models import Category,Product,Brand,ColorAd,SizeAd,Price,Collection
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
    brand_filter = request.GET.get('brands')
    color_filter = request.GET.get('colors')
    size_filter = request.GET.get('sizses')
    price_filter = request.GET.get('prices')
    sort_by = request.GET.get('sort_by', 'featured')
    collection_filter = request.GET.get('collection')
    products = Product.objects.all()

    # Применение фильтров
    if brand_filter:
        products = products.filter(brand__title=brand_filter)
    if color_filter:
        # Используйте related_name `product_color_ad` для фильтрации по цвету
        products = products.filter(product_color_ad__settings__title=color_filter)
    if size_filter:
        products = products.filter(sizead__al=size_filter)
    if price_filter:
        try:
            # Преобразуем строку в число для фильтрации
            max_price = float(price_filter.replace(',', '.'))
            products = products.filter(price__lte=max_price)
        except ValueError:
            # В случае ошибки преобразования строки в число, игнорируем фильтр цены
            pass
    if collection_filter:
        products = products.filter(collection__title=collection_filter)
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
    prices = Price.objects.all()
    collections = Collection.objects.all()

     # Настройка пагинации
    paginator = Paginator(products, 20)  # Показывать 10 продуктов на странице
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

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