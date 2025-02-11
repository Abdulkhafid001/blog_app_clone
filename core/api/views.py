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



