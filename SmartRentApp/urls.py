from django.contrib import admin
from django.urls import path
from SmartRentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('reset/', views.reset, name='reset'),
    path('home/', views.index, name='home'),
    path('accommodations/', views.accommodations, name='accommodations'),

]
