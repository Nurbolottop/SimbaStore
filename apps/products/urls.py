from django.urls import path  

from apps.products import views

urlpatterns = [
    path("clothes", views.shop, name="shop"),
    path("clothes/<int:id>/", views.shop_detail, name="shop_detail"),

]