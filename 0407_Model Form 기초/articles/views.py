from django.shortcuts import redirect, render

from .forms import ArticleForm
from .models import Article

# Create your views here.


def index(request):
    # 입력한 모든 정보 불러오기 ..
    # 이거 모델로 불러왔던거같다
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
            'form' : form,
            'article' : article,
        }
    return render(request, 'articles/update.html', context)


