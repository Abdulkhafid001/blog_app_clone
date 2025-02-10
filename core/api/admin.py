from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Like)
