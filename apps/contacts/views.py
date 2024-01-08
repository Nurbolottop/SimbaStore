from django.shortcuts import render,redirect
from datetime import datetime

################################################################################################################################################################################

from apps.contacts import models
from apps.base.models import Settings,Category
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
    settings = models.Settings.objects.latest("id")
    category = models.Category.objects.latest("id")
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
            subscriber = models.Subscriber.objects.create(email = email)
            return redirect( 'index')
    return render(request,'base/contact.html', locals())