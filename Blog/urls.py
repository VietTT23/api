from django.urls import path, include
from .views import BlogListView
from .route import *
urlpatterns = [
    path('list/view/<p>', BlogListView, name='BlogListView')

]

