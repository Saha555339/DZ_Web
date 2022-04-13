from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('<int:i>', views.question, name="question"),
    path('ask/', views.ask, name="ask"),
    path('log', views.log_in, name="log-in"),
    path('registration', views.registration, name="registration"),
    path('settings', views.settings, name="settings")
]
