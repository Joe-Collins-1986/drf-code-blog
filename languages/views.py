from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Language
from .serializers import LanguageDetailSerializer, LanguageSerializer

class LanguageList(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Language.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LanguageDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Language.objects.all()