from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.starting_page, name='starting_page'),
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug_>/', views.post_detail, name='post_detail'),
    path('autors/', views.authors_list, name='authors_list'),
    path('autors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:tag_id>/', views.tag_posts, name='tag_posts'),
]


handler404 = views.custom_404_page
