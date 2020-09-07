from django.shortcuts import render

from article.models import Article


def index(request):
    context = {
        'articles': Article.objects.is_import(),
        'trend': Article.objects.filter(status='publish').order_by('-view_count')[:4]
    }
    return render(request, 'index.html', context=context)

def detail(request, id):
    article = Article.objects.get(pk=id)
    article.view_count += 1
    article.save()
    context = {
        'article': article
    }
    return render(request, 'blog-single.html', context=context)