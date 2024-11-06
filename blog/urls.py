from . import views
from django.urls import path

from .views import (
    NewComment,
    EditComment,
    DeleteComment,
)

urlpatterns = [
    path('',  views.PostList.as_view(), name='news'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/', views.NewComment.as_view(), name='new_comment'),
    path('edit/<int:pk>/', views.EditComment.as_view(), name='edit_comment'),
    path('delete/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),
]