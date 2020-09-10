from django.urls import path
from article import views as article_views

app_name = 'article'

urlpatterns = [
    path('', article_views.ArticleListView.as_view(), name='home'),
    path('<str:slug>/', article_views.ArticleDetailView.as_view(), name='article-detail'),
    # path('article/<int:id>/', article_views.detail, name='article-detail'),
]

