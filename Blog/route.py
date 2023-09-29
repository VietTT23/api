from rest_framework.routers import SimpleRouter, DefaultRouter
from .rest_view import PostListView

class ShareApiRouter(SimpleRouter):
    share_router = DefaultRouter()
    def register(self, *args, **kwargs):
        self.share_router.register(*args, **kwargs)
        super().register(*args, **kwargs)

route = ShareApiRouter().share_router

route.register(r'blog/post/all', PostListView, basename='PostListView')