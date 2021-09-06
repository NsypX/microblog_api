from django.urls import path
from .views import post_opps, post_by_id, post_like,post_dislike,post_insert_n_random_posts

urlpatterns = [
    path('posts/', post_opps),
    path('posts/<int:pk>', post_by_id),
    path('posts_like/<int:pk>', post_like),
    path('posts_dislike/<int:pk>', post_dislike),
    path('insert_n_posts/<int:n>', post_insert_n_random_posts),
]
