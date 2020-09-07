from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
