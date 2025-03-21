from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/blogposts/",  BlogPostList.as_view(), name="blog-post-create"),
    path("api/blogposts/<int:post_id>",  BlogPostCreateViewFrontend.as_view(), name="blog-post-create"),

    path("api/author/<int:author_id>/blogposts", get_author_posts, name="author posts"),

    path("api/blogposts/<int:post_id>/like", LikeBlogPostView.as_view(), name="like blogpost"),
    
    path("api/blogposts/<int:post_id>/comment", CommentBlogPostView.as_view(), name="comment blogpost"),
    path("api/blogposts/<int:post_id>/share", ShareBlogPostView.as_view(), name="like blogpost"),


    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/testuser/", get_user_info, name="user info"),
    
    
    path("api/blogposts/signup", sign_up, name="sign up"),
    path("api/blogposts/follow", follow_user, name="follow")
]
