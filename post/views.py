from django.shortcuts import render
from rest_framework.generics import ListAPIView

from post.models import Post
from post.pagination import MyPagination
from post.serializers import PostSerializers


class PostListAPIView(ListAPIView):
    model = Post
    pagination_class = MyPagination
    serializer_class = PostSerializers

    def get_queryset(self):
        return Post.objects.all()
