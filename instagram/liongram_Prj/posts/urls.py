from django.urls import path
from .views import detail, list, create, update, delete, result

urlpatterns = [
    path('', list, name = "list"),
    path('create/', create, name = "create"),
    path('result/', result, name = "result"),
    path('detail/<int:id>/', detail, name = "detail" ),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]