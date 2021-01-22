from django.contrib import admin
from django.urls import path
from basicapp import views

app_name="basicapp"

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('login/', views.user_login, name="user_login"),
]
