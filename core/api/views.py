from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'


@api_view(['GET', 'POST'])
def blogpost_list(request):
    """ post a blog post to the API."""

    if request.method == 'GET':
        blogposts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostCreateViewFrontend(APIView):
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        blogposts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     blogpost = BlogPost.objects.get(pk=pk)
    #     serializer = BlogPostSerializer(blogpost, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     blogpost = BlogPost.objects.get(pk=pk)
    #     blogpost.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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
        user_name = request.POST["userName"]
        user_mail = request.POST["userMail"]
        user_password = request.POST["password"]
        print(user_name)
        # return Response({'message': 'signed up succesfully'})
    return HttpResponse('login here') 
