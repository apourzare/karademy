from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article import views as article_views
from karademy import views as main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_view.index, name='home'),
    path('', main_view.HomeView.as_view(), name='home'),
    path('article/', include('article.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
