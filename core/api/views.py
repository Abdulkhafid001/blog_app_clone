from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset  = BlogPost.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
