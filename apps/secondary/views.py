from django.shortcuts import render
from apps.base import models

# Create your views here.
def index(request):
    settings = models.Settings.objects.all()
    return render(request,'base/index-2.html', request)