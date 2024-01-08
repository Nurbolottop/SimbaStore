from django.shortcuts import render,redirect

################################################################################################################################################################################

from apps.contacts import models
from apps.base.models import Settings,Category
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
            return redirect( 'index')
        if "reviews" in request.POST:
            title = request.POST.get('title')
            message = request.POST.get('message')
            review = models.Review.objects.create(title = title,message=message)
            return redirect( 'index')
        
    return render(request,'secondary/reviews.html', locals())