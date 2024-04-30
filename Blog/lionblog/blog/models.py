from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50) #글의 제목
    content = models.TextField() # 글의 본문
    created_at = models.DateTimeField(auto_now_add=True) #생성일자

    def __str__(self):
        return f'[{self.id}] {self.title}'