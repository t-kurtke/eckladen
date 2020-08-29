from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/update', views.PostUpdate.as_view(), name='post_update'),
    path("posts/<user_name>/", views.posts_user, name="posts_user"),
    path('<category_name>/', views.blog_category, name='blog_category'),
    path("create/post/", views.PostCreate.as_view(), name="post_create"),
    path('postimage_delete/<int:pk>/', views.postimage_delete, name='postimage_delete')

]