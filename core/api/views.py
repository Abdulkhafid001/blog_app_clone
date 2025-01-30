from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
