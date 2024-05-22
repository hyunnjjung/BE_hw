from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


def create(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('accounts:login') 

        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymous') == 'on'

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                anonymity=anonymity
            )
            return redirect('post:create')
        else:
            return render(request, 'post/list.html', {'error': 'Title and Content are required.'})

    posts = Post.objects.all().order_by('-id')
    return render(request, 'post/list.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'post/detail.html', {'post' :post})

@login_required
def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:detail', id)
    return render(request, 'post/update.html', {'post': post})
    

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:create')
    


