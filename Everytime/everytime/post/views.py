from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required

def posts_list(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')
    return render(request, 'post/post_list.html', {'category': category, 'posts': posts, 'categories': categories, })


def list(request):
    categories = Category.objects.all()
    
    category_in_posts = {}
    for category in categories:
        posts = category.posts.order_by('-id')
        category_in_posts[category] = posts

    return render(request, 'post/list.html', {'category_in_posts': category_in_posts, 'categories' : categories})


@login_required
def create(request):
    categories = Category.objects.all() 

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')  == 'on'

        categories_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in categories_ids]

        post = Post.objects.create(
            title = title,
            content = content,
            anonymity = anonymity,
            author = request.user,
        )

        for category in category_list:
            post.category.add(category)

        return redirect('post:list')
    return render(request, 'post/post_list.html', {'categories': categories})


@login_required
def create(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)  # 해당 slug에 해당하는 카테고리 가져오기
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('accounts:login') 
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymous') == 'on'

        # 새로운 글 생성
        new_post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            anonymity=anonymity
        )
        # 해당 글을 카테고리와 연결
        new_post.save()  # 먼저 저장해야 새로운 포스트의 id가 생성됨
        new_post.category.add(category)  # ManyToMany 필드에 추가

        return redirect('post:list')  # 글 목록 페이지로 이동

    return render(request, 'post/list.html', {'categories': categories, 'category': category})


def detail(request, id):
    post = get_object_or_404(Post, id = id)
    return render(request, 'post/detail.html', {'post' :post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:detail', id)
    return render(request, 'post/update.html', {'post' :post})
    

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post:list')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('post:detail', comment.post.id)
    

def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)

    anonymity = request.POST.get('anonymous') == 'on'

    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post,
            anonymity = anonymity
        )
        return redirect('post:detail', post_id)

def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.add(request.user)
    return redirect('post:detail', post_id)

def remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.remove(request.user)
    return redirect('post:detail', post_id)

def mylike(request):
    liked_posts = Post.objects.filter(like=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':liked_posts})

def add_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.add(request.user)
    return redirect('post:detail', post_id)

def remove_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.remove(request.user)
    return redirect('post:detail', post_id)

def myscrap(request):
    scraped_posts = Post.objects.filter(scrap=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':scraped_posts})

