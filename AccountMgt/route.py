from rest_framework.routers import SimpleRouter, DefaultRouter
from .rest_view import PostListView

from Blog.route import ShareApiRouter


route = ShareApiRouter().share_router

route.register(r'blog/post/all', PostListView, basename='PostListView')