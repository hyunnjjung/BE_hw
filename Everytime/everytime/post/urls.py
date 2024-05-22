from django.urls import path
from .views import create, detail, update, delete

app_name = 'post'
urlpatterns = [
    path('', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail" ),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]