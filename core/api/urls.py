from django.urls import path
from api.views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy

urlpatterns = [
    path("api/blogposts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("api/blogposts/<int:pk>", BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
]
