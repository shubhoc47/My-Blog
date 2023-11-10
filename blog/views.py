from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from lorem_text import lorem
# Create your views here.

multi_posts = [{
    "slug": "wondering-in-the-forest",
    "image": "blog/images/first_post.jpg",
    "author": "Shubho Chowdhury",
    "date": date(2021, 7, 21),
    "title": "Exploring forest",
    "excerpt": lorem.sentence(),
    "content": lorem.paragraphs(3)
},
{
    "slug": "walking-on-the-seabeach",
    "image": "blog/images/second_post.jpg",
    "author": "Sayem Mollah",
    "date": date(2022, 7, 21),
    "title": "Beautiful seabeach",
    "excerpt": lorem.sentence(),
    "content": lorem.paragraphs(3)
},
{
    "slug": "hiking-in-the-mountain",
    "image": "blog/images/third_post.jpeg",
    "author": "Saad",
    "date": date(2020, 7, 21),
    "title": "Mountain Hiking",
    "excerpt": lorem.sentence(),
    "content": lorem.paragraphs(3)
},
{
    "slug": "walking-in-the-rain",
    "image": "blog/images/fourth_post.jpg",
    "author": "Mamu",
    "date": date(2023, 7, 21),
    "title": "Rain falling",
    "excerpt": lorem.sentence(),
    "content": lorem.paragraphs(3)
}]

def fun(post):
    return post['date']

def index(request):
    sorted_posts = sorted(multi_posts, key=fun)
    return render(request, 'blog/index.html',{
        "posts": sorted_posts[-3:]
    })

def posts(request):
    return render(request, 'blog/all-posts.html',{
        "posts": multi_posts,
    })

def single_post(request, slug):
    
    try:
        post = next(post for post in multi_posts if post['slug'] == slug)

        return render(request, 'blog/single-post.html',{
            "post": post
        })
    except:
        return render(request, '404.html')
