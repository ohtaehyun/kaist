from django.urls import path
from .views import post_list

app_name = 'blog'

urlpatterns = [
    path('list', post_list)
]
