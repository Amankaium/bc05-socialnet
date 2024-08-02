from django.urls import path
from posts.views import *


urlpatterns = [
    path("list/", PostsList.as_view(), name="posts-list"),
    path('info/<int:pk>/', PostInfo.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
]
