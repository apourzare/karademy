from django.shortcuts import render
from article.models import Article
from django.views.generic.list import ListView


# def index(request):
#     context = {
#         'articles': Article.objects.is_import(),
#         'trend': Article.objects.filter(status='publish').order_by('-view_count')[:4]
#     }
#     return render(request, 'index.html', context=context)

class HomeView(ListView):
    queryset = Article.objects.is_import()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trend'] = Article.objects.filter(status='publish').order_by('-view_count')[:4]
        context['new_article'] = Article.objects.filter(status='publish').last()
        return context