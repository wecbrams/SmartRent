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
    path('about/', views.about, name='about'),
    path('book/<int:accommodation_id>/', views.book_accommodation, name='book_accommodation'),
    path('booking-success/', views.booking_success, name='booking_success'),

]
