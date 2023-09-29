from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, generics, status, filters, serializers
from .serializer import PostSerializer
from .models import Post
from rest_framework.pagination import PageNumberPagination

class MediumPageSize(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 1000


class PostListView(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    queryset = Post.objects.all().order_by("-updated_at")
    pagination_class = MediumPageSize
    lookup_field = 'id'
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        return instance.delete()
