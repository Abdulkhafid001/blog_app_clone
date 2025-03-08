from datetime import timezone
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


def default_imageurl():
    return "https://imgs.search.brave.com/XGdJ4-IfhuybNdfZgNJK7LWugrtpad9RemRulqyzjfI/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA5LzYzLzk3LzY3/LzM2MF9GXzk2Mzk3/NjcwNV9JV2ZEQWNY/M3VxNVJFUmVSYnhi/WU5aNXpxeTdjMVA3/Ni5qcGc"


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_image_url = models.URLField(null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='author', default=1)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_author', null=True)
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='like_author', null=True)
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='likes')
    likes = models.IntegerField(default=0)
    date_and_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username


class Share(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='share_author', null=True)
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='shares')
    shares = models.IntegerField(default=0)
    date_and_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.name


class Follow(models.Model):
    follower = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='followers')
    followed = models.ForeignKey(
        Author, related_name='following', on_delete=models.CASCADE)
    followers_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower} followed {self.followed}"
