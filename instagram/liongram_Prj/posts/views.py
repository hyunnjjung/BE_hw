from django.shortcuts import render
from .models import Post
from django.db.models import Q
# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'posts/list.html', {'posts': posts})


def result(request):
    if 'data' in request.GET:
        post = request.GET['data']
        posts = Post.objects.filter( Q(title__contains=post) | Q(content__contains=post)).order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')

    return render(request, 'posts/search.html', {'data': post, 'posts': posts})

