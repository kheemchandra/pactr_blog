from django.urls import path 

from . import views 
from .feeds import LatestPostFeed

app_name = 'blog'



urlpatterns = [

    path('search/', views.post_search, name='post_search'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/<slug:slug>/',views.post_detail, name='post_detail'),
    path('share/<int:post_id>/', views.post_share, name='post_share'),
    path('<str:tag>/', views.post_list, name='post_tag'),
    path('latest/feed/', LatestPostFeed(), name='latest_feed'),
    
]