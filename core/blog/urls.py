from django.urls import path
from blog.views import ItemListCreateView

urlpatterns = [
    # path('', views.index, name='index'),
    path("items/", ItemListCreateView.as_view(), name="item-list-create"),
]
