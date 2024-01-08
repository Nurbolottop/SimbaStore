from django.urls import path  

################################################################################################################################################################################

from apps.secondary import views

urlpatterns = [
    path('about/', views.about,name="about"),
    path('faqs/', views.faqs,name="faqs"),

]