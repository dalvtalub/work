from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index),
                  path('about_us', views.about_us),
                  path('add_article', include('add_article.urls')),
                  path('articles', views.articles),
                  path('team_lineup/<str:team1>__<str:team2>', views.team_lineup, name='teams'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
