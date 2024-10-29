from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.home, name='bl-home'),
    path('about/', views.about, name='bl-about'),
    path('logout/', views.logout_view, name='logout'),

]