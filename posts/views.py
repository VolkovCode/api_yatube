from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()    
    
    def list(self, request, pk=None):
        serializer = PostSerializer(self.queryset, many=True)
        if request.user.is_authenticated:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def partial_update(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if request.user == post.author:
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:    
            return Response(status=status.HTTP_403_FORBIDDEN) 
    
    def destroy(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:        
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

     
class CommentViewSet(viewsets.ModelViewSet):  
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()    
               
    def list(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data) 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)   

    def partial_update(self, request, post_id, pk=None):
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.author:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:    
            return Response(status=status.HTTP_403_FORBIDDEN)      
  
    def destroy(self, request, post_id, pk=None):
        comment = Comment.objects.get(pk=pk)
        if comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:        
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            