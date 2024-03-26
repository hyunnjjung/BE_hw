
from django.contrib import admin
from django.urls import path
from wordCountApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('wordCount/', views.wordCount, name="wordCount"),
    path('result/', views.result, name="result"),
    path('hello/', views.hello, name="hello"),
]
