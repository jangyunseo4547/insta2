from django.urls import path
from .import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),

    # comment_create
    path('<int:post_id>/comments/create', views.comment_create, name='comment_create'),

    # 좋아요
    path('<int:post_id>/like/', views.like, name='like'),
]

