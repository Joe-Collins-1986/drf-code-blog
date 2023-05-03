from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    Update later
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Update later
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
