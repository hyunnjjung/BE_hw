from django.db import models
from user.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length= 20)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

class Post(models.Model):
    title = models.CharField(max_length=50) #글의 제목
    content = models.TextField() # 글의 본문
    created_at = models.DateTimeField(auto_now_add=True) #생성일자
    anonymity = models.BooleanField(default=True) # 익명
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField(to= Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to=User, through="Like", related_name="liked_posts")
    scrap = models.ManyToManyField(to=User, through="Scrap", related_name="scraped_posts")

    def __str__(self):
        return f'[{self.id}] {self.title}'
    

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")  # corrected here
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    anonymity = models.BooleanField(default=True) # 익명
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'

    
class PostCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="categories_postcategory")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="post_postcategory")


class Like(models.Model):
    post = models.ForeignKey(to= Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_likes")

class Scrap(models.Model):
    post = models.ForeignKey(to= Post, on_delete=models.CASCADE, related_name="post_scraps")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_scraps")