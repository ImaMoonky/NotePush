from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    path('', views.home,name='hub-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about,name='hub-about'),
    path('note/', views.NoteCanvas,name='hub-Canvas'),
    path('blog/', PostListView.as_view(),name='hub-blog'),
    # we are making a new line that will go to a specific post
    # TO do this we add variables to routes
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]
