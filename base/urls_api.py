
from base.views_api import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView)
]


