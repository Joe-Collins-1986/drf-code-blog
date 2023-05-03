from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Article
from .serializers import ArticleSerializer

class ArticleList(generics.ListCreateAPIView):
    """
    Update later
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Article.objects.annotate(
        comments_count = Count('comments', distinct=True),
        likes_count = Count('likes', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'owner__username',
        'art_title',
    ]

    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at', #REMOVE IN FINAL PROJECT
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update later
    """
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.annotate(
        comments_count = Count('comments', distinct=True),
        likes_count = Count('likes', distinct=True)
    ).order_by('-created_at')
