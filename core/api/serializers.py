from django.db.models import Sum
from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    total_shares = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ['id', 'title', 'content',
                  'post_image_url', 'pub_date', 'author', 'total_likes', 'total_comments', 'total_shares']

    def get_total_likes(self, obj):
        return obj.likes.aggregate(total_likes=Sum('likes'))['total_likes'] or 0

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_shares(self, obj):
        return obj.shares.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'
