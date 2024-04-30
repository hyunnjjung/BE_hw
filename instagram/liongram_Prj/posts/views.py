from django.shortcuts import get_object_or_404, redirect, render
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


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content
        )

        return redirect('list')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id = id)

    post.count += 1
    post.save()

    return render(request, 'posts/detail.html', {'post' :post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    return render(request, 'posts/update.html', {'post' :post})
    

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('list')

