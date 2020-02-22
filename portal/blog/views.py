from django.shortcuts import render
from .models import Content
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
