from django.urls import path, include
from app import views

urlpatterns = [
    path('question/<int:i>', views.question, name="question"),
    path('ask', views.ask, name="ask"),
    path('login', views.log_in, name="log-in"),
    path('registration', views.registration, name="registration"),
    path('settings', views.settings, name="settings"),
    path('hot', views.hot_questions, name="hot_questions")
]
