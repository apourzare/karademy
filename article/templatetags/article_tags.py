from django import template
from article.models import Article

register = template.Library()

@register.inclusion_tag('article/customtags/published_articles.html')
def published_articles():
    articles = Article.objects.filter(status='publish')
    return { 'articles': articles }