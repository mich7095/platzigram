"""platzigram URL Configuration
"""
#Django
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from platzigram import views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi),

    path('posts/', posts_views.list_posts, name='feed'),

    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
