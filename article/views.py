from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from article.models import Article


def index(request):
    return render(request, 'article/categories.html')

def detail(request, id):
    article = Article.objects.get(pk=id)
    # article.view_count += 1
    # article.save()
    context = {
        'article': article
    }
    return render(request, 'blog-single.html', context=context)

class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        self.object.view_count += 1
        self.object.save()
        self.object.refresh_from_db()
        return context
