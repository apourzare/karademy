from django.urls import reverse_lazy
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from article.models import Article, Category


# def index(request):
#     return render(request, 'article/categories.html')

# def detail(request, id):
#     article = Article.objects.get(pk=id)
#     # article.view_count += 1
#     # article.save()
#     context = {
#         'article': article
#     }
#     return render(request, 'blog-single.html', context=context)

class ArticleListView(ListView):
    # model = Article
    queryset = Article.objects.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(status=True)
        return context


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        if self.object.status == 'publish':
            self.object.view_count += 1
            self.object.save()
            self.object.refresh_from_db()
        return context


class ArticleCreateView(CreateView):
    model = Article
    fields = [
        'ro_titre', 
        'title', 
        'slug', 
        'abstruct', 
        'status', 
        'author', 
        'body', 
        'thumbnail', 
        'category', 
        'is_important'
        ]
    success_url = '/article/'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = [
        'ro_titre', 
        'title', 
        'slug', 
        'abstruct', 
        'status', 
        'author', 
        'body', 
        'thumbnail', 
        'category', 
        'is_important'
    ]
    success_url = '/article/{slug}'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:home')