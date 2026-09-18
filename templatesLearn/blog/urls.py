from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('details/', views.blog_details, name='blog-details'),
    path('list/', views.blog_list, name='blog-list'),
]
