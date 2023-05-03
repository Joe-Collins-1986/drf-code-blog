from django.db.models import Count
from rest_framework import generics, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProfileList(generics.ListAPIView):
    """
    Update later
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        article_count = Count('owner__article', distinct=True),
        followed_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),
        languages_count = Count('owner__language', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile', #FOLLOWERS
        'owner__followed__owner__profile', #FOLLOWING
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'languages_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Update later
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        article_count = Count('owner__article', distinct=True),
        followed_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True),
        languages_count = Count('owner__language', distinct=True),
    ).order_by('-created_at')
