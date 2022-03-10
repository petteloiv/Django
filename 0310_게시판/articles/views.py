from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.

def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Articles(title=title, content=content)
    article.save()
    return redirect('detail', article.pk)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('detail', article.pk)

def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    else:
        return redirect('detail', article.pk)
