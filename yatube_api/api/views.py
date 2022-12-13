from posts.models import Group, Post, Follow, User
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer, GroupSerializer
from .serializers import PostSerializer, FollowSerializer
from rest_framework.permissions import IsAuthenticated
from .user_viewset import CreateListViewSet
from .user_permissions import IsAuthorOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = get_object_or_404(Post, pk=int(post_id)).comments
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=int(self.kwargs.get("post_id")))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateListViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        new_queryset = get_object_or_404(
            User,
            username=self.request.user
        ).follower
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
