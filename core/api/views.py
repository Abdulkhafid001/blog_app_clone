import json
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


class BlogPostList(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class BlogPostCreateViewFrontend(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, post_id):
        blogpost = BlogPost.objects.get(id=post_id)
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)

    def put(self, request, post_id):
        blogpost = BlogPost.objects.get(id=post_id)
        serializer = BlogPostSerializer(blogpost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        blogpost = BlogPost.objects.get(id=post_id)
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeBlogPostView(APIView):
    def post(self, request, post_id):
        try:
            post = BlogPost.objects.get(id=post_id)
            like, created = Like.objects.get_or_create(
                user=post.author, blog_post=post)

            if not created:
                like.likes += 1
                like.save()
            serializer = BlogPostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({"error": "BlogPost not found"}, status=status.HTTP_404_NOT_FOUND)


class CommentBlogPostView(APIView):
    def post(self, request, post_id):
        try:
            post = BlogPost.objects.get(id=post_id)
            comment = Comment.objects.create(
                user=post.author, blog_post=post, content=request.data['content'])
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({"error": "BlogPost not found"}, status=status.HTTP_404_NOT_FOUND)


class ShareBlogPostView(APIView):
    def post(self, request, post_id):
        try:
            post = BlogPost.objects.get(id=post_id)
            share, created = Share.objects.get_or_create(
                user=post.author, blog_post=post)

            if not created:
                share.shares += 1
                share.save()

            serializer = ShareSerializer(share)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({"error": "BlogPost not found"}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_name = data.get('userName')
        user_mail = data.get('userEmail')
        password = data.get('userPassword')

        try:
            user = User.objects.create_user(
                username=user_name, email=user_mail, password=password)
            user.save()
        except:
            pass
    return JsonResponse({'message': 'signed up succesfully'})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request):
    print(request.user)
    data = json.loads(request.body)
    username = data.get('userName')
    main_user = Author.objects.get(id=1)
    user_to_follow = get_object_or_404(Author, name=username)
    follow, created = Follow.objects.get_or_create(
        follower=main_user, followed=user_to_follow)
    if created:
        follow.followers_count += 1
        follow.save()
    elif not created:
        pass
    FollowersSerializer(follow)
    return JsonResponse({'message': "follow successful"})


def unfollow_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        user = Author.objects.get(id=1)
        user_to_unfollow = get_object_or_404(Author, name=username)
        Follow.objects.filter(
            follower=user, followed=user_to_unfollow).delete()
    pass


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
    })


# get author detail page
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_author_posts(request, author_id):
    author = Author.objects.get(id=author_id)
    all_posts = BlogPost.objects.filter(author=author)
    serializer = AuthorSerializer(author)
    serializer2 = BlogPostSerializer(all_posts, many=True)
    return Response(serializer2.data)
