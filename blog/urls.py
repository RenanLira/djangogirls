from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit' ),
    path('rascunhos/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:id>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:id>/remove/', views.post_remove, name='post_remove'),
    path('comment/<int:id>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
]