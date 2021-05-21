from django.urls import path
from opensource import views

urlpatterns = [
    path('', views.getAllPosts),
    path('post/<int:pk>', views.getPost, name='post'),
    path('post/create/', views.newPost),
    path('post/edit/<postId>', views.editPost),
    path('post/delete/<postId>', views.deletePost),
    path('like/<int:pk>', views.likePost, name='like_post'),
]   