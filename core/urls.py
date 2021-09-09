from os import name
from core.views import HomeView, RegisterView
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView

admin.site.site_header = 'Админ панель'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name="logout")
]
