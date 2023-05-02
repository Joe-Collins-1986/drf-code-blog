from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ArticleList(APIView):
    serializer_class = ArticleSerializer
    permission_classes = [
            permissions.IsAuthenticatedOrReadOnly
        ]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(
            articles,
            many=True,
            context={
                'request': request
                })
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(
            data=request.data,
            context={
                'request': request
                })
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    

class ArticleDetail(APIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)
            return article
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(
            article,
            context={
                'request': request
                })
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(
            article, data=request.data,
            context={
                'request': request
                })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)