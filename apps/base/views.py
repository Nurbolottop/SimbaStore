from django.shortcuts import render
from datetime import datetime

################################################################################################################################################################################

from apps.base import models
from apps.secondary.models import Slide,LookBook

# Create your views here.
def index(request):
#Base
    settings = models.Settings.objects.latest("id")
    category = models.Category.objects.latest("id")
    sale = models.Sale.objects.all()

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
#Secondary
    lookbook = LookBook.objects.latest("id")
    slide = Slide.objects.all()
    return render(request,'base/index-2.html', locals())