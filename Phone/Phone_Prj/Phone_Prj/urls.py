
from django.contrib import admin
from django.urls import path
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list, name = "list"),
    path('result', views.result, name = "result")
]
