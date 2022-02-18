from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.PostListView.as_view(), name='post_list'), # instead of
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',  # for sending emails
         views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),  # it call for the post_list function but with tag_slug parameter
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),


]

"""
Creating a urls.py file for each application is the best way to 
make your applications reusable by other projects.

"""

# path('', views.PostListView.as_view(), name='post_list'), i delete that because i replace class based view
