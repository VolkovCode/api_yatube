from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField( source="author.username", read_only=True)
    #text = serializers.CharField(source="post.text", max_length=500)
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        fields = ('id', 'author', 'post', 'created', 'text')  
        model = Comment      