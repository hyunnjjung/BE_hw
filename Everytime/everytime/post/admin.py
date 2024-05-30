from django.contrib import admin

from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post) #모델 admin에 등록