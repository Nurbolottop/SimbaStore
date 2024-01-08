from django.shortcuts import render

################################################################################################################################################################################

from apps.base import models
from apps.secondary.models import Slide,LookBook

# Create your views here.
def index(request):
#Base
    settings = models.Settings.objects.latest("id")
#Secondary
    lookbook = LookBook.objects.latest("id")
    slide = Slide.objects.all()
    return render(request,'base/index-2.html', locals())