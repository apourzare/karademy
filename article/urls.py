from django.urls import path
from article import views as article_views

app_name = 'article'

urlpatterns = [
    path('', article_views.ArticleListView.as_view(), name='home'),
    path('create/', article_views.ArticleCreateView.as_view(), name='article-create'),
    path('<str:slug>/', article_views.ArticleDetailView.as_view(), name='article-detail'),
    path('<pk>/edit/', article_views.ArticleUpdateView.as_view(), name='article-update'),
    path('<pk>/delete/', article_views.ArticleDeleteView.as_view(), name='article-delete'),
    
    # path('article/<int:id>/', article_views.detail, name='article-detail'),
]

