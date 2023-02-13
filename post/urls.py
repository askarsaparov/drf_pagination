from django.urls import path, include

from post.views import PostListAPIView

urlpatterns = [
    path("", PostListAPIView.as_view()),
]