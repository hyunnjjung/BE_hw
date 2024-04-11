from django.urls import path
from .views import *

urlpatterns = [
    path('', List.as_view(), name = "list"),
    path('result', Result.as_view(),  name = "result"),
]



