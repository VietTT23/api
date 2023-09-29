from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from Blog.models import Post

def BlogListView(requests,p, *args, **kwargs):
    respones = {}
    respones['status'] = 'Fail'
    list_view = [
        "id",
        "title",
        "content",
        "created_by",
        "updated_by",
    ]
    if requests.method == "GET":
        blog_objs = Post.objects.all().order_by("-updated_at")
        if len(blog_objs) > 0:
            blog_list = list(blog_objs.values(*list_view))
            respones['status'] = 'OK'
            page = Paginator(blog_list, '10')
            results = page.page(p)

            respones['results'] = list(results)
        else:
            respones['status'] = 'False'


    return JsonResponse(respones)