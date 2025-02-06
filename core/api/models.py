from django.db import models


class Author(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='blog_posts', default=1)

    def __str__(self):
        return self.title
