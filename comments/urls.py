from django.urls import path
from comments.views import *


urlpatterns = [
    path('v1/list/', CommentList.as_view()),
    path('v1/create/', CommentCreateAPIView.as_view()),
    path('v1/detail/<int:pk>/', CommentDetailAPIView.as_view()),
    path('v1/update/<int:pk>/', CommentUpdateAPIView.as_view()),
    path('v1/delete/<int:pk>/', CommentDeleteAPIView.as_view()),
    
    path('v2/list-create/', CommentListCreate.as_view()), 
    path('v2/info/<int:pk>/', CommentInfo.as_view()),
    
]