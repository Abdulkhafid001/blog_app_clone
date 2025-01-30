from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
