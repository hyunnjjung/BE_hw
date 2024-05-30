from django.urls import path
from . import views
from .views import add_scrap, delete_comment, list, create, detail, myscrap, remove_scrap, update, delete, create_comment, add_like, remove_like, mylike

app_name = 'post'
urlpatterns = [
    path('', list, name = "list"),
    path('create/<slug:slug>', views.create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail" ),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
    path('delete-comment/<int:comment_id>', delete_comment, name = "delete-comment"),
    path('create-comment/<int:post_id>/', create_comment, name = "create-comment"),
    path('add-like/<int:post_id>/', add_like, name = "add-like"),
    path('remove-like/<int:post_id>/', remove_like, name = "remove-like"),
    path('my-like/', mylike, name = "my-like"),
    path('add-scrap/<int:post_id>/', add_scrap, name = "add-scrap"),
    path('remove-scrap/<int:post_id>/', remove_scrap, name = "remove-scrap"),
    path('my-scrap/', myscrap, name = "my-scrap"),
    path('<slug:slug>/', views.posts_list, name='posts_list')
    
]