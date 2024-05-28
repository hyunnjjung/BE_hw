from django.contrib import admin
from .models import Post, Comment, Category


admin.site.register(Post) #모델 admin에 등록
admin.site.register(Comment) #모델 admin에 등록
admin.site.register(Category) #모델 admin에 등록