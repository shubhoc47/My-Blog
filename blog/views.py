from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from lorem_text import lorem
from .models import Post, Author, Tag
# Create your views here.


def index(request):
    multi_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html',{
        "posts": multi_posts
    })

def posts(request):
    multi_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html',{
        "posts": multi_posts,
    })

def single_post(request, slug):
    
    try:
        post = Post.objects.get(slug=slug)

        return render(request, 'blog/single-post.html',{
            "post": post,
            "tags": post.tag.all()
        })
    except:
        return render(request, '404.html')
