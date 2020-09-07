from django.urls import path
from article import views as article_views

urlpatterns = [
    path('', article_views.index, name='home'),
    path('article/<int:id>/', article_views.detail, name='article')
]

