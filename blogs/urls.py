from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path('', views.index, name='index'),
    path('my-posts', views.home, name='home'),
    path('my-posts/article/<int:post_id>/', views.full_article, name='article'),
    path('my-posts/add-new-posts', views.add_topic, name='add_post'),
    path('my-posts/article/<int:post_id>/edit-this-post', views.edit_post, name='edit_post'),
    path('my-posts/delete-post/<int:post_id>/', views.delete_post, name="delete_post")
]
