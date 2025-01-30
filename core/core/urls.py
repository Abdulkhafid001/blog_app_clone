from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("blog/", include("api.urls")),
    path('admin/', admin.site.urls),
]
