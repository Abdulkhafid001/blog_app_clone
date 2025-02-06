from django.urls import path
from api.views import *

urlpatterns = [
    path("api/blogposts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("api/blogposts/<int:pk>", BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path("api/authors/", AuthorListCreate.as_view(), name="blogpost-view-create"),
    path("api/authors/<int:pk>", AuthorRetrieveUpdateDestroy.as_view(), name="update"),
]
