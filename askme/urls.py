from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('', include("app.urls")),
    path('tag/<int:number>', views.tags_question, name="tag")
]
