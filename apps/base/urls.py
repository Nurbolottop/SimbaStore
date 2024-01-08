from django.urls import path  
from apps.base import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("blog_detail/<int:id>/", views.blog_detail, name="blog_detail"),
]