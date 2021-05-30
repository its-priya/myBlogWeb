from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('details/', views.details, name='details'),
]