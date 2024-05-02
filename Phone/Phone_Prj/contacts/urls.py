from django.urls import path
from .views import create, detail, update, delete, List, Result

urlpatterns = [
    path('', List.as_view(), name = "list"),
    path('result', Result.as_view(),  name = "result"),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail" ),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]



