from django.db.models import Sum
from rest_framework import serializers
from .models import *


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['user']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['user', 'name', 'email'] 


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['id', 'author_name', 'content', 'blog_post', 'pub_date']

    def get_author_name(self, obj):
        return obj.user.name


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        # fields = '__all__'
        fields = ['user', 'blog_post', 'shares', 'date_and_time']


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    total_shares = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ['id', 'title', 'content',
                  'post_image_url', 'pub_date', 'author', 'author_name', 'total_likes', 'total_comments', 'total_shares', 'comments']

    def get_total_likes(self, obj):
        return obj.likes.aggregate(total_likes=Sum('likes'))['total_likes'] or 0

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_shares(self, obj):
        # return obj.shares.count()
        return obj.shares.aggregate(total_shares=Sum('shares'))['total_shares'] or 0

    def get_author_name(self, obj):
        return obj.author.name
