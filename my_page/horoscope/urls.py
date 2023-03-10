from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_info_about_types),
    path('type/<str:type_zodiac>/', views.get_info_about_type_zodiac, name = 'zodiac_type'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_numbers),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name = 'horoscope_name'),
]