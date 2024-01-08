from django.urls import path  

################################################################################################################################################################################

from apps.contacts import views

urlpatterns = [
    path('reviews/', views.reviews,name="reviews")
]