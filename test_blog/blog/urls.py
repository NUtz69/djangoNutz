from django.urls import path
from blog import views


urlpatterns = [
    # Index post list
    path('', views.PostListView.as_view(), name='post_list'),
    # About
    path('about/', views.AboutView.as_view(), name='about'),
    # Post detail
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # Create new post
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    # Update edit post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(),
         name='post_edit'),
    # Delete post
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(),
         name='post_remove'),
    # Drafts
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    # Add comment
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # Comment approve
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    # Comment delete
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # Post publish
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # Search
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
