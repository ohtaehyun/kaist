from django.urls import path
from .views import post_list,mysum

app_name = 'blog'

urlpatterns = [
    path('post_list', post_list),
    path('sum/<int:a>/<int:b>',mysum)
]
