from django.urls import path
from api.views import *

urlpatterns = [
    # path("api/blogposts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
    # path("api/blogposts/<int:pk>", BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path("api/authors/", AuthorListCreate.as_view(), name="blogpost-view-create"),
    path("api/authors/<int:pk>", AuthorRetrieveUpdateDestroy.as_view(), name="update"),

    # custom URL routes
    path("blogposts/",  BlogPostCreateViewFrontend.as_view(), name="blog-post-create"),
    path("blogposts/<int:post_id>/like", LikeBlogPostView.as_view(), name="like blogpost"),
    path("blogposts/<int:post_id>/comment", CommentBlogPostView.as_view(), name="comment blogpost"),
    path("blogposts/<int:post_id>/share", ShareBlogPostView.as_view(), name="like blogpost"),
    path("blogposts/signup", sign_up, name="sign up"),
]
