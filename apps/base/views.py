from django.shortcuts import render

################################################################################################################################################################################

from apps.base import models
from apps.secondary.models import Slide

# Create your views here.
def index(request):
    settings = models.Settings.objects.latest("id")
    slide = Slide.objects.all()
    return render(request,'base/index-2.html', locals())