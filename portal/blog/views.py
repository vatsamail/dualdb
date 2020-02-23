from django.shortcuts import render
from .models import Content, Post, Category
# Create your views here.


def test(request):
    return render(request, 'hello_world.html', {})

def content_index(request):
    contents = Content.objects.all()
    context = {
        'contents': contents
    }
    return render(request, 'content_index.html', context)


def content_detail(request, pk):
    content = Content.objects.get(pk=pk)
    context = {
        'content': content
    }
    return render(request, 'content_detail.html', context)


def post_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_index.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)
