"""platzigram URL Configuration
"""
#Django
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from platzigram import views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),

    path('posts/', posts_views.list_posts),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
